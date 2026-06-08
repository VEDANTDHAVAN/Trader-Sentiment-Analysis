import pandas as pd


def create_features(df):

    numeric_cols = [
        "Size USD",
        "Closed PnL",
        "Fee"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df["win"] = (
        df["Closed PnL"] > 0
    ).astype(int)

    df["loss"] = (
        df["Closed PnL"] < 0
    ).astype(int)

    df["absolute_pnl"] = (
        df["Closed PnL"].abs()
    )

    df["net_pnl"] = (
        df["Closed PnL"]
        - df["Fee"]
    )

    df["large_trade"] = (
        df["Size USD"]
        > df["Size USD"].median()
    ).astype(int)

    return df