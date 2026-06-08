import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_pnl_distribution(df):
    plt.figure(figsize=(8,5))

    sns.boxplot(
        x="Classification",
        y="Closed PnL", data=df
    )

    plt.title("PnL Distribution by Sentiment")

    plt.savefig("outputs/pnl_distribution.png")

    plt.close()

def plot_win_rate(df):
    win_df = (
        df.groupby(
            "Classification"
        )["win"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8,5))

    sns.barplot(
        data=win_df, y="win",
        x="Classification"
    )

    plt.title("Win Rate by Sentiment")
    plt.savefig("outputs/win_rate.png")

    plt.close()

def plot_trade_size(df):

    plt.figure(figsize=(8,5))

    sns.boxplot(
        x="Classification",
        y="Size USD",
        data=df
    )

    plt.title(
        "Trade Size Distribution"
    )

    plt.savefig(
        "outputs/trade_size.png"
    )

    plt.close()

def feature_importance_plot(feature_df: pd.DataFrame):
    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=True
    )

    plt.figure(figsize=(8, 5))

    plt.barh(
        feature_df["Feature"],
        feature_df["Importance"]
    )

    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Feature Importance")

    plt.tight_layout()

    plt.savefig(
        "outputs/feature_importance.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        "Saved: outputs/feature_importance.png"
    )