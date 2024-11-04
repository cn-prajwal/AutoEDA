import pandas as pd

def data_summary(df):
    # Ensure the 'Data Type' column is being created based on actual data types
    summary = {
        'Mean': df.mean(),
        'Median': df.median(),
        'Std Dev': df.std(),
        'Min': df.min(),
        'Max': df.max(),
        'Data Type': df.dtypes  # This should give you the data type of each column
    }
    return pd.DataFrame(summary)


def missing_values(df):
    """Identify missing values in the DataFrame."""
    return pd.DataFrame({
        'Missing Count': df.isnull().sum(),
        'Missing Percentage': (df.isnull().mean() * 100).round(2)
    })

def correlation_analysis(df):
    """Calculate the correlation matrix of the DataFrame."""
    return df.corr()
