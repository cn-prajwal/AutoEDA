import pandas as pd

def data_summary(df):
    """Generate a summary of the DataFrame."""
    return pd.DataFrame({
        'Data Type': df.dtypes,
        'Non-null Count': df.notnull().sum(),
        'Unique Count': df.nunique(),
        'Mean': df.mean(),
        'Std': df.std(),
        'Min': df.min(),
        '25%': df.quantile(0.25),
        '50%': df.median(),
        '75%': df.quantile(0.75),
        'Max': df.max()
    })

def missing_values(df):
    """Identify missing values in the DataFrame."""
    return pd.DataFrame({
        'Missing Count': df.isnull().sum(),
        'Missing Percentage': (df.isnull().mean() * 100).round(2)
    })

def correlation_analysis(df):
    """Calculate the correlation matrix of the DataFrame."""
    return df.corr()
