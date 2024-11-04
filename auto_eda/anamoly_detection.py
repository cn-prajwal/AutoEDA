import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy import stats

def detect_outliers_zscore(df):
    z_scores = stats.zscore(df)
    abs_z_scores = abs(z_scores)
    return df[(abs_z_scores > 3).any(axis=1)]

def detect_outliers_isolation_forest(df, contamination=0.05):
    model = IsolationForest(contamination=contamination)
    model.fit(df)
    outliers = model.predict(df)
    return df[outliers == -1]
