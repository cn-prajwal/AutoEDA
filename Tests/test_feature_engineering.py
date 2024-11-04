import pandas as pd
from auto_eda.feature_engineering import suggest_encoding, recursive_feature_elimination, suggest_feature_combinations

def test_suggest_encoding():
    df = pd.DataFrame({
        'A': ['a', 'b', 'a', 'c'],
        'B': [1, 2, 3, 4]
    })
    suggestions = suggest_encoding(df)
    assert suggestions['A'] == 'Consider One-Hot or Label Encoding'

def test_recursive_feature_elimination():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7]
    })
    X = df[['A', 'B']]  # Make sure to include more than one feature
    y = df['B']
    selected_features = recursive_feature_elimination(X, y)


def test_suggest_feature_combinations():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7],
        'C': [7, 8, 9, 10]
    })
    suggestions = suggest_feature_combinations(df, correlation_threshold=0.9)
    assert len(suggestions) == 0  # No pairs should exceed the threshold
