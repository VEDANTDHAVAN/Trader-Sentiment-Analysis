import pandas as pd

def load_data(sentiment_path, trade_path):
    sentiment = pd.read_csv(sentiment_path)
    trades = pd.read_csv(trade_path)

    return sentiment, trades