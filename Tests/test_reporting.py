import pandas as pd
from auto_eda.reporting import generate_custom_report
import os

def test_generate_custom_report(tmp_path):
    df = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': [5, 6, 7, 8]
    })
    output_file = tmp_path / "report.html"
    generate_custom_report(df, output_file=str(output_file))
    assert os.path.exists(output_file)  # Check if report file was created
