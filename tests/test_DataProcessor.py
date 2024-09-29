# import sys
# import os

# # Add src to sys.path for testing purposes
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
import pandas as pd
from exampleproject.class_example import DataFrameProcessor

# Test cases for DataFrameProcessor

def test_init_with_dict():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    processor = DataFrameProcessor(data)
    assert isinstance(processor.data, pd.DataFrame), "Data should be converted to a DataFrame"

def test_init_with_dataframe():
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    processor = DataFrameProcessor(data)
    assert processor.data.equals(data), "The DataFrame should remain unchanged"

def test_show_data(capsys):
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    processor = DataFrameProcessor(data)
    processor.show_data()
    captured = capsys.readouterr()
    assert "Current DataFrame" in captured.out, "The printed output should contain 'Current DataFrame'"
    assert "col1" in captured.out, "The printed output should display the data columns"
    
def test_add_column():
    data = {'col1': [1, 2, 3]}
    processor = DataFrameProcessor(data)
    processor.add_column('col2', [4, 5, 6])
    assert 'col2' in processor.data.columns, "New column 'col2' should be added"
    assert processor.data['col2'].tolist() == [4, 5, 6], "The values of 'col2' should be [4, 5, 6]"

def test_add_column_mismatch():
    data = {'col1': [1, 2, 3]}
    processor = DataFrameProcessor(data)
    with pytest.raises(ValueError, match="The length of values must match the number of rows in the DataFrame"):
        processor.add_column('col2', [4, 5])  # Intentional length mismatch

def test_get_summary():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    processor = DataFrameProcessor(data)
    summary = processor.get_summary()
    assert isinstance(summary, pd.DataFrame), "The summary should be a DataFrame"
    assert 'col1' in summary.columns, "The summary should include 'col1'"
    assert 'col2' in summary.columns, "The summary should include 'col2'"