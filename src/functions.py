
from statsmodels.tsa.deterministic import DeterministicProcess, CalendarFourier
import pandas as pd
from sklearn.linear_model import LinearRegression

def make_deterministic_features(y, train_start=None, train_end=None,
    order=2, fourier_order=5, model=LinearRegression(fit_intercept=False)):
    """
    Create deterministic (trend + Fourier seasonal) features
    for a time series y (with a PeriodIndex or DatetimeIndex).

    Parameters:
        y : pd.Series
            target time series with a proper time index.
        order : int, default=2
            polynomial trend order (1 = linear, 2 = quadratic).
        fourier_order : int, default=5
            number of Fourier harmonics for annual seasonality.
        model : default=LinearRegression()

    Returns:
        dp : DeterministicProcess
            The fitted deterministic process object (for forecasting later).
        X_dp : pd.DataFrame
            in-sample deterministic features aligned to y.
    """
    fourier_year = CalendarFourier(freq="A", order=fourier_order)
    fourier_week = CalendarFourier(freq="W", order=3)

    dp = DeterministicProcess(
        index=y.index,
        constant=True,
        order=order,
        seasonal=False,
        additional_terms=[fourier_year, fourier_week],
        drop=True,
    )
    X_dp = dp.in_sample()

    # choose fit window
    if (train_start is not None) and (train_end is not None):
        X_dp_train = X_dp.loc[train_start:train_end]
        y = y.loc[train_start:train_end]

    else:
        X_dp_train = X_dp

    # Fit trend model
    model.fit(X_dp_train, y)

    # fit and return fit-window outputs
    y_hat_fit = pd.DataFrame(
        model.predict(X_dp_train),
        index=y.index,
        columns=y.columns
    )

    y_resid = y - y_hat_fit

    return dp, X_dp, model, y_hat_fit, y_resid, X_dp_train


def make_residual_features(y, calendar_df, holidays, lags=[1,2,7,14,21,28], windows=[7,30,365]):
    """
        create lag and rolling features for residual modeling,
        and combine with calendar/holiday features.

        Parameters:
            y : pd.Series
                Target time series with proper time index.
            calendar_df : pd.DataFrame
                Calendar features (dow, is_weekend, month, etc.).
            holidays :
                Holiday features (is_holiday).
            lags : list of int
                lags (in periods) to include.
            windows : list of int
                rolling window sizes for mean/std.

        Returns:
            X : pd.DataFrame
                feature matrix (lags, rolling, calendar, holiday).
        """
    X = pd.DataFrame(index=y.index)

    # lags
    for lag in lags:
        X[f"lag_{lag}"] = y.shift(lag)

    # rolling mean/std
    for w in windows:
        r = y.rolling(window=w)
        X[f"roll{w}_mean"] = r.mean()
        X[f"roll{w}_std"] = r.std()

    # holidays
    X['is_holiday'] = y.index.isin(holidays).astype(int)

    # calendar
    X = X.join(calendar_df)

    return X