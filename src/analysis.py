import pandas as pd

# 1. Sentiment vs Profitability
def sentiment_pnl(df):
    return (
        df.groupby("Classification")["Closed PnL"]
        .agg(["count", "mean", "median", "sum"])
    )

# 2. Win Rate
def win_rate(df):
    return (
        df.groupby("Classification")["win"]
        .mean() * 100
    )

# 3. Trade Size Analysis
def trade_size_analysis(df):
    return (
        df.groupby("Classification")
        ["Size USD"].describe()
    )

# Buy vs Sell
def side_analysis(df):
    return pd.crosstab(
        df["Classification"], df["Side"],
        normalize="index"
    ) * 100

# 5. Long vs Short
def direction_analysis(df):
    return pd.crosstab(
        df["Classification"],
        df["Direction"], normalize="index"
    ) * 100

# 6. Top Traders
def top_traders(df):
    return (
        df.groupby("Account")
        ["Closed PnL"].sum().sort_values(
            ascending=False
        ).head(20)
    )

# 7. Profitability by Coin
def coin_analysis(df):
    return (
        df.groupby("Coin")["Closed PnL"]
        .sum().sort_values(ascending=False)
    )

# 8. Coin Sentiment Analysis
def coin_sentiment_analysis(df):
    return pd.pivot_table(
        df, values="Closed PnL", index="Coin",
        columns="Classification", aggfunc="mean"
    )

# 9. Trader Segmentation
def trader_segmentation(df):
    trader_stats = (
        df.groupby("Account").agg(
            Total_PnL=("Closed PnL", "sum"),
            Trades=("Trade ID", "count")
        )
    )

    trader_stats["Rank"] = (
        trader_stats["Total_PnL"].rank(pct=True)
    )

    trader_stats["Segment"] = "Middle"

    trader_stats.loc[
        trader_stats["Rank"] >= 0.90,
        "Segment"
    ] = "Top"

    trader_stats.loc[
        trader_stats["Rank"] <= 0.10,
        "Segment"
    ] = "Bottom"

    return trader_stats