import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

def detect_outliers_zscore(df, threshold=3):
    # Calculate the z-scores for each value in the dataframe
    z_scores = df.apply(zscore)
    # Identify rows where any z-score exceeds the threshold
    outliers = df[(z_scores.abs() > threshold).any(axis=1)]
    return outliers

def detect_outliers_isolation_forest(df, contamination=0.05):
    model = IsolationForest(contamination=contamination)
    model.fit(df)
    outliers = model.predict(df)
    return df[outliers == -1]
