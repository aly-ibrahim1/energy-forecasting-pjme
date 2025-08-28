import pandas as pd

def load_data(path="../data/raw/PJME_hourly.csv", to_period=False, granularity="daily"):
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

    if granularity == "daily":
        df = df.resample("D").sum()

        if to_period:
            df = df.to_period("D")

    elif granularity == "monthly":
        df = df.resample("M").sum()

        if to_period:
            df = df.to_period("M")

    elif granularity == "weekly":
        df = df.resample("W").sum()

        if to_period:
            df = df.to_period("W")

    elif granularity == "yearly":
        df = df.resample("Y").sum()

        if to_period:
            df = df.to_period("Y")

    return df
