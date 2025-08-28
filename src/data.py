import pandas as pd

def load_data(path="../data/raw/PJME_hourly.csv", to_period=False):
    """
    Load PJME hourly CSV -> daily sum series.
    - Parses Datetime
    - Averages duplicate timestamps
    - Sets time index
    - Aggregates to daily sum
    - Optional PeriodIndex
    """
    df = pd.read_csv(path, parse_dates=["Datetime"])
    df = df.groupby("Datetime", as_index=False)["PJME_MW"].mean()  # resolve dupes by averaging
    df = df.set_index("Datetime").sort_index()
    daily = df.resample("D").sum()                                # total daily consumption

    if to_period:
        daily = daily.to_period("D")

    return daily
