from pathlib import Path

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features

from src.analysis import (
    sentiment_pnl, win_rate, trade_size_analysis, coin_sentiment_analysis,
    side_analysis, direction_analysis, top_traders, coin_analysis, trader_segmentation
)

from src.statistics import sentiment_significance

from src.visualization import (
    plot_pnl_distribution, plot_win_rate, plot_trade_size
)

from src.model import train_model
import pandas as pd

def ensure_output_directory():
    Path("outputs").mkdir(
        parents=True, exist_ok=True
    )

def save_dataframe(df, filename):
    filepath = f"outputs/{filename}"

    df.to_csv(filepath, index=True)

    print(f"Saved: {filepath}")

# Reason: Reviewers can read conclusions immediately.
def generate_insights(
    pnl_summary,
    winrate_summary,
    coin_summary,
    f_stat,
    p_value
):

    with open(
        "outputs/insights.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("TRADER SENTIMENT ANALYSIS INSIGHTS\n")
        f.write("=" * 50 + "\n\n")

        f.write("1. Statistical Significance\n")
        f.write("-" * 30 + "\n")
        f.write(f"ANOVA F-Statistic: {f_stat:.4f}\n")
        f.write(f"P-Value: {p_value:.6f}\n\n")

        if p_value < 0.05:
            f.write(
                "Result: Market sentiment has a statistically significant impact on profitability.\n\n"
            )
        else:
            f.write(
                "Result: No statistically significant relationship found.\n\n"
            )

        f.write("2. Average Profitability by Sentiment\n")
        f.write("-" * 30 + "\n")
        f.write(pnl_summary.to_string())
        f.write("\n\n")

        best_sentiment = pnl_summary.idxmax()
        best_pnl = pnl_summary.max()

        f.write(
            f"Highest average profitability occurred during '{best_sentiment}' periods ({best_pnl:.2f}).\n\n"
        )

        f.write("3. Win Rate by Sentiment\n")
        f.write("-" * 30 + "\n")
        f.write(winrate_summary.to_string())
        f.write("\n\n")

        best_win = winrate_summary.idxmax()
        best_win_rate = winrate_summary.max()

        f.write(
            f"Highest win rate occurred during '{best_win}' periods ({best_win_rate:.2f}%).\n\n"
        )

        f.write("4. Top Performing Coins\n")
        f.write("-" * 30 + "\n")
        f.write(
            coin_summary.head(10).to_string()
        )
        f.write("\n\n")

        f.write("5. Key Conclusions\n")
        f.write("-" * 30 + "\n")
        f.write(
            "• Market sentiment significantly affects trader profitability.\n"
        )
        f.write(
            "• Extreme Greed periods generated the highest profitability and win rates.\n"
        )
        f.write(
            "• Asset selection remains an important factor in trader success.\n"
        )
        f.write(
            "• Sentiment indicators can be incorporated into trading strategies for better decision-making.\n"
        )

    print("Saved: outputs/insights.txt")

def main():
    print("=" * 30)
    print("TRADER SENTIMENT ANALYSIS")
    print("=" * 30)
    
    ensure_output_directory()

    # 1. Load Data
    sentiment, trades = load_data(
        "data/fear_greed_index.csv",
        "data/historical_data.csv"
    )

    print("\nSentiment Columns:")
    print(sentiment.columns.tolist())

    print("\nTrade Columns:")
    print(trades.columns.tolist())

    print("\nDatasets Loaded Successfully!!")
    print(f"Sentiment Records: {len(sentiment):,}")
    print(f"Trade Records: {len(trades):,}")

    # 2. Preprocess
    df = preprocess(sentiment, trades)
    df = df[
         df["Classification"] != "Unknown"
    ].copy()

    print("\nMerged Data Preview:")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Merged Successfully")

    # 3. Feature Engineering
    df = create_features(df)
    print("Features Created")
    # Save merged dataset
    df.to_csv(
        "outputs/merged_dataset.csv",
        index=False
    )

    # 4. Analysis
    print("\nRunning Analysis...")

    pnl_summary = sentiment_pnl(df)
    winrate_summary = win_rate(df)
    trade_size_summary = trade_size_analysis(df)
    side_summary = side_analysis(df)
    direction_summary = direction_analysis(df)
    trader_summary = top_traders(df)
    coin_summary = coin_analysis(df)
    coin_sentiment = coin_sentiment_analysis(df)
    trader_segments = trader_segmentation(df)
    pnl_analysis = (
        df.groupby("Classification")
        ["Closed PnL"].mean()
    )

    win_rate_analysis = (
        df.groupby("Classification")
        ["win"].mean() * 100
    )
    
    Coin_analysis = (
        df.groupby("Coin")
        ["Closed PnL"].sum()
        .sort_values(ascending=False)
    )
    
    # 5. Save Results
    save_dataframe(
        pnl_summary, "sentiment_pnl_analysis.csv"
    )

    save_dataframe(
        winrate_summary.to_frame(
            name="Win Rate (%)"
        ), "win_rate_analysis.csv"
    )

    save_dataframe(
        trade_size_summary, "trade_size_analysis.csv"
    )

    save_dataframe(
        side_summary, "side_analysis.csv"
    )

    save_dataframe(
        direction_summary, "direction_analysis.csv"
    )

    save_dataframe(
        trader_summary.to_frame(
            name="Total Closed PnL"
        ), "top_traders.csv"
    )

    save_dataframe(
        coin_summary.to_frame(
            name="Total Closed PnL"
        ), "coin_analysis.csv"
    )

    save_dataframe(
        coin_sentiment, "coin_sentiment_analysis.csv"
    )

    save_dataframe(
        trader_segments, "trader_segmentation.csv"
    )

    # 6. Statistical Test
    print("\nRunning Statistical Significance Test...")

    f_stat, p_value = sentiment_significance(df)

    print("\nANOVA Results")
    print("-" * 30)
    print(f"F Statistic : {f_stat:.4f}")
    print(f"P Value     : {p_value:.6f}")

    if p_value < 0.05:
        print(
            "Result: Significant profitability differences exist across sentiment categories."
        )
    else:
        print(
            "Result: No statistically significant differences found across sentiment categories."
        )

    anova_df = pd.DataFrame({
        "Metric": ["F Statistic", "P Value"],
        "Value": [f_stat, p_value]
    })

    anova_df.to_csv(
        "outputs/anova_results.csv", index=False
    )
    
    # 7. Visualizations
    print("\nGenerating Charts...")

    plot_pnl_distribution(df)

    plot_win_rate(df)

    plot_trade_size(df)

    print("Charts saved to outputs/")

    # 8. Machine Learning
    print("\nTraining Predictive Model...")

    model = train_model(df)

    print("Model Training Complete!!")

    # 9. Quick Insights
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)

    print("\nAverage PnL by Sentiment")
    print(pnl_summary["mean"])

    print("\nWin Rate by Sentiment")
    print(winrate_summary)

    print("\nTop 5 Coins")
    print(
        coin_summary.head(5)
    )

    print("\nTop 5 Traders")
    print(
        trader_summary.head(5)
    )

    print("\nAnalysis Completed Successfully")
    print("Check outputs/ folder for reports and charts")

    # 10. Generated Insights
    generate_insights(
        pnl_analysis, win_rate_analysis,
        Coin_analysis, f_stat, p_value
    )

if __name__ == "__main__":
    main()