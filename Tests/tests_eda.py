import pandas as pd
from auto_eda.eda import data_summary, missing_values, correlation_analysis

def test_data_summary():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, None, 8],
        'C': ['a', 'b', 'c', 'd']
    })
    summary = data_summary(df)
    assert summary['Data Type']['A'] == 'int64'
    assert summary['Non-null Count']['B'] == 3
    assert summary['Mean']['A'] == 2.5

def test_missing_values():
    df = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': [None, 'b', 'c', 'd']
    })
    missing = missing_values(df)
    assert missing['Missing Count']['A'] == 1
    assert missing['Missing Percentage']['B'] == 25.0

def test_correlation_analysis():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
    })
    correlation = correlation_analysis(df)
    assert correlation.shape == (2, 2)  # Should be a 2x2 matrix
