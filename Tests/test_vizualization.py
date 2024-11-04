import pandas as pd
from auto_eda.visualization import plot_pairplot, plot_correlation_heatmap, plot_histogram, plot_3d_scatter

def test_plot_pairplot():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7]
    })
    try:
        plot_pairplot(df)
    except Exception as e:
        assert False, f"plot_pairplot raised an exception: {e}"

def test_plot_correlation_heatmap():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7]
    })
    try:
        plot_correlation_heatmap(df)
    except Exception as e:
        assert False, f"plot_correlation_heatmap raised an exception: {e}"

def test_plot_histogram():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4]
    })
    try:
        plot_histogram(df, 'A')
    except Exception as e:
        assert False, f"plot_histogram raised an exception: {e}"

def test_plot_3d_scatter():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7],
        'C': [7, 8, 9, 10]
    })
    try:
        plot_3d_scatter(df, 'A', 'B', 'C')
    except Exception as e:
        assert False, f"plot_3d_scatter raised an exception: {e}"
