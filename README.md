# Auto-EDA

![image](https://github.com/user-attachments/assets/654a7dcf-97c1-4f48-b69c-daad1e95eb91)

## Overview
**Auto-EDA** is a Python library designed to streamline the exploratory data analysis (EDA) process, providing automated and user-friendly tools for summarizing, visualizing, detecting anomalies, and engineering features in datasets. This library is ideal for data analysts and data scientists looking for quick insights into their data without having to write repetitive EDA code.

## Features
- **Data Summary**: Automated summary of DataFrame properties, including column types, non-null counts, unique counts, and descriptive statistics.
- **Visualizations**: Built-in functions for generating pair plots, correlation heatmaps, histograms, and 3D scatter plots.
- **Anomaly Detection**: Outlier detection using Z-score and Isolation Forest algorithms.
- **Feature Engineering**: Suggestions for encoding, recursive feature elimination, and correlation-based feature combinations.
- **Automated Reporting**: Generate HTML-based profiling reports using `pandas-profiling`.

## Installation
To install the library, use `pip`:
```bash
pip install auto_eda
```

## Directory Structure
Your project directory should look like this:
```
auto_eda/
├── auto_eda/
│   ├── __init__.py
│   ├── eda.py                
│   ├── visualization.py       
│   ├── anomaly_detection.py   
│   ├── feature_engineering.py 
│   ├── reporting.py
│   ├── config.py
├── tests/
│   ├── test_eda.py
│   ├── test_visualization.py
│   ├── test_anomaly_detection.py
│   └── test_feature_engineering.py
├── docs/
│   └── (Sphinx documentation files)
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
└── setup.py
```

## Quick Start Guide
Here's an example of how to use the Auto-EDA library for a sample dataset:

```python
import pandas as pd
from auto_eda import data_summary, plot_pairplot

# Load your data
df = pd.read_csv('your_data.csv')

# Generate a data summary
summary = data_summary(df)
print(summary)

# Visualize relationships in the data
plot_pairplot(df, hue='target_column')  # Replace 'target_column' with the column you want to use for color coding
```

### Example of Automated Reporting
Generate a full profile report and save it as an HTML file:
```python
from auto_eda.reporting import generate_profile_report

generate_profile_report(df, output_file='data_report.html')
```

## Module Descriptions

- **`eda.py`**: Functions for generating data summaries, identifying missing values, and calculating correlation matrices.
- **`visualization.py`**: Functions for creating various visualizations such as pair plots, correlation heatmaps, histograms, and 3D scatter plots.
- **`anomaly_detection.py`**: Functions for detecting outliers using Z-score and Isolation Forest.
- **`feature_engineering.py`**: Provides feature encoding suggestions, recursive feature elimination, and correlation-based feature combinations.
- **`reporting.py`**: Generates an interactive HTML-based data profiling report.
- **`config.py`**: Stores configuration settings for the EDA process, including output format and plotting preferences.

## Running Tests
To run the tests for this library, ensure `pytest` is installed, then run:
```bash
pytest tests/
```

## Documentation
Documentation is generated using Sphinx. To build it:

1. Navigate to the `docs` directory.
2. Run `make html` to generate HTML documentation.
3. Open the `docs/_build/html/index.html` file in your browser.

## Contribution Guidelines
We welcome contributions to improve Auto-EDA! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or suggestions, feel free to open an issue on GitHub.
