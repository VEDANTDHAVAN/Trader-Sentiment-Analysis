from typing import Tuple, cast
from scipy.stats import ttest_ind


def sentiment_significance(df) -> Tuple[float, float]:

    fear = df[
        df["Classification"] == "Fear"
    ]["Closed PnL"]

    greed = df[
        df["Classification"] == "Greed"
    ]["Closed PnL"]

    result = ttest_ind(
        fear,
        greed,
        equal_var=False
    )

    statistic = cast(float, result[0])
    pvalue = cast(float, result[1])

    return statistic, pvalue