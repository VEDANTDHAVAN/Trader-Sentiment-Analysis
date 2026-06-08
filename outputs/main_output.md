==============================              
TRADER SENTIMENT ANALYSIS        
==============================
   
Sentiment Columns: 
['timestamp', 'value', 'classification', 'date']
                  
Trade Columns:
['Account', 'Coin', 'Execution Price', 'Size Tokens', 'Size USD', 'Side', 'Timestamp IST', 'Start Position', 'Direction', 'Closed PnL','Transaction Hash', 'Order ID', 'Crossed', 'Fee', 'Trade ID', 'Timestamp']

Datasets Loaded Successfully!!
Sentiment Records: 2,644
Trade Records: 211,224
Invalid timestamps: 0

Merged Records: 211,224

Sentiment Distribution:
Classification
Fear             61837
Greed            50303
Extreme Greed    39992
Neutral          37686
Extreme Fear     21400
Unknown              6
Name: count, dtype: int64

Merged Data Preview:
                                      Account  ... Classification
0  0xae5eacaf9c6b9111fd53034a602c192a04e082ed  ...  Extreme Greed
1  0xae5eacaf9c6b9111fd53034a602c192a04e082ed  ...  Extreme Greed
2  0xae5eacaf9c6b9111fd53034a602c192a04e082ed  ...  Extreme Greed
3  0xae5eacaf9c6b9111fd53034a602c192a04e082ed  ...  Extreme Greed
4  0xae5eacaf9c6b9111fd53034a602c192a04e082ed  ...  Extreme Greed

[5 rows x 18 columns]

Columns:
['Account', 'Coin', 'Execution Price', 'Size Tokens', 'Size USD', 'Side', 'Timestamp IST', 'Start Position', 'Direction', 'Closed PnL','Transaction Hash', 'Order ID', 'Crossed', 'Fee', 'Trade ID', 'Timestamp', 'Date', 'Classification']

Data Merged Successfully
Features Created

Running Analysis...
Saved: outputs/sentiment_pnl_analysis.csv
Saved: outputs/win_rate_analysis.csv
Saved: outputs/trade_size_analysis.csv
Saved: outputs/side_analysis.csv
Saved: outputs/direction_analysis.csv
Saved: outputs/top_traders.csv
Saved: outputs/coin_analysis.csv
Saved: outputs/coin_sentiment_analysis.csv
Saved: outputs/trader_segmentation.csv

Running Statistical Significance Test...

ANOVA Results
------------------------------
F Statistic : 9.0622
P Value     : 0.000000
Result: Significant profitability differences exist across sentiment categories.

Generating Charts...
Charts saved to outputs/

Training Predictive Model...

Feature Importance
          Feature  Importance
5       Direction    0.528323
3            Coin    0.167010
2             Fee    0.120469
1        Size USD    0.109571
4            Side    0.053787
0  Classification    0.020839
              precision    recall  f1-score   support

           0       0.96      0.93      0.95     24848
           1       0.91      0.94      0.93     17396

    accuracy                           0.94     42244
   macro avg       0.93      0.94      0.94     42244
weighted avg       0.94      0.94      0.94     42244

Model Training Complete!!

============================================================
KEY INSIGHTS
============================================================

Average PnL by Sentiment
Classification
Extreme Fear     34.537862
Extreme Greed    67.892861
Fear             54.290400
Greed            42.743559
Neutral          34.307718
Name: mean, dtype: float64

Win Rate by Sentiment
Classification
Extreme Fear     37.060748
Extreme Greed    46.494299
Fear             42.076750
Greed            38.482794
Neutral          39.699093
Name: win, dtype: float64

Top 5 Coins
Coin
@107    2.783913e+06
HYPE    1.948485e+06
SOL     1.639556e+06
ETH     1.319979e+06
BTC     8.680447e+05
Name: Closed PnL, dtype: float64

Top 5 Traders
Account
0xb1231a4a2dd02f2276fa3c5e2a2f3436e6bfed23    2.143383e+06
0x083384f897ee0f19899168e3b1bec365f52a9012    1.600230e+06
0xbaaaf6571ab7d571043ff1e313a9609a10637864    9.401638e+05
0x513b8629fe877bb581bf244e326a047b249c4ff1    8.404226e+05
0xbee1707d6b44d4d52bfe19e41f8a828645437aab    8.360806e+05
Name: Closed PnL, dtype: float64

Analysis Completed Successfully
Check outputs/ folder for reports and charts