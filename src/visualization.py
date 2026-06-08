import matplotlib.pyplot as plt
import seaborn as sns

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