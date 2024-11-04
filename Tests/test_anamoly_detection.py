import pandas as pd
from auto_eda.anamoly_detection import detect_outliers_zscore, detect_outliers_isolation_forest

def test_detect_outliers_zscore():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 100],  # Outlier
        'B': [5, 6, 7, 8, 9]
    })
    outliers = detect_outliers_zscore(df)
    assert len(outliers) == 1  # Should detect one outlier

def test_detect_outliers_isolation_forest():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 100],  # Outlier
        'B': [5, 6, 7, 8, 9]
    })
    outliers = detect_outliers_isolation_forest(df)
    assert len(outliers) == 1  # Should detect one outlier
