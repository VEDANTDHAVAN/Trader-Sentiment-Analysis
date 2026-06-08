# Replace the t-test with ANOVA.

# Reason:
# 5 sentiment classes exist

# ANOVA is statistically correct.
from scipy.stats import f_oneway


def sentiment_significance(df):

    groups = []

    for sentiment in df["Classification"].unique():

        group = df[
            df["Classification"]
            == sentiment
        ]["Closed PnL"]

        groups.append(group)

    f_stat, p_value = f_oneway(*groups)

    return f_stat, p_value