import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

def suggest_encoding(df):
    suggestions = {}
    for column in df.select_dtypes(include=['object', 'category']):
        suggestions[column] = 'Consider One-Hot or Label Encoding'
    return suggestions

def recursive_feature_elimination(X, y, n_features_to_select=1):
    model = LinearRegression()
    rfe = RFE(estimator=model, n_features_to_select=n_features_to_select)  # Fix initialization
    rfe.fit(X, y)
    return X.columns[rfe.support_]

def suggest_feature_combinations(df, correlation_threshold=0.9):
    corr_matrix = df.corr()
    suggestions = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > correlation_threshold:
                suggestions.append((corr_matrix.columns[i], corr_matrix.columns[j]))
    return suggestions

