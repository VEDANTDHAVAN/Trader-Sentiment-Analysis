from pathlib import Path

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features

from src.analysis import (
    sentiment_pnl, win_rate, trade_size_analysis, 
    side_analysis, direction_analysis, top_traders, coin_analysis
)

from src.statistics import sentiment_significance

from src.visualization import (
    plot_pnl_distribution, plot_win_rate, plot_trade_size
)

from src.model import train_model

def ensure_output_directory():
    Path("outputs").mkdir(
        parents=True, exist_ok=True
    )

def save_dataframe(df, filename):
    filepath = f"outputs/{filename}"

    df.to_csv(filepath, index=True)

    print(f"Saved: {filepath}")

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

    # 6. Statistical Test
    print("\nRunning Statistical Significance Test...")

    statistic, pvalue = sentiment_significance(df)

    print("\nT-Test Results")
    print("-" * 30)

    print(f"T Statistic : {statistic:.4f}")

    print(f"P Value     : {pvalue:.6f}")

    if pvalue < 0.05:
        print(
            "Result: Significant difference "
            "between Fear and Greed profitability."
        )
    else:
        print(
            "Result: No statistically significant "
            "difference found."
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

if __name__ == "__main__":
    main()