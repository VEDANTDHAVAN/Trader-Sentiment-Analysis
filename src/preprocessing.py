import pandas as pd


def preprocess(sentiment, trades):
    # Clean column names
    sentiment.columns = sentiment.columns.str.strip()
    trades.columns = trades.columns.str.strip()

    # Sentiment Dataset
    sentiment["date"] = pd.to_datetime(
        sentiment["date"]
    )

    sentiment = sentiment.rename(
        columns={
            "date": "Date",
            "classification": "Classification"
        }
    )

    # Keep only required columns
    sentiment = sentiment[
        ["Date", "Classification"]
    ]

    # Trade Dataset
    trades["Timestamp IST"] = pd.to_datetime(
        trades["Timestamp IST"], dayfirst=True, errors="coerce", format="mixed"
    )
    
    print(
       f"Invalid timestamps: "
       f"{trades['Timestamp IST'].isna().sum():,}"
    )

    trades["Date"] = (
        trades["Timestamp IST"]
        .dt.normalize()
    )

    # Merge
    merged = trades.merge(
        sentiment,
        on="Date",
        how="left"
    )

    # Handle Missing Values
    merged["Classification"] = (
        merged["Classification"]
        .fillna("Unknown")
    )

    print(f"\nMerged Records: {len(merged):,}")

    print("\nSentiment Distribution:")

    print(
        merged["Classification"]
        .value_counts()
    )

    return merged