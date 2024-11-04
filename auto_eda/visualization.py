import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_pairplot(df, hue=None):
    sns.pairplot(df, hue=hue)
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.show()

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()

def plot_3d_scatter(df, x, y, z, color=None):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=color)
    fig.show()
