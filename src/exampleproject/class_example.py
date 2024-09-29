# complex_example_class.py

import numpy as np
import pandas as pd

# Base class
class DataFrameProcessor:
    def __init__(self, data):
        """
        Constructor that initializes the DataFrame.
        Expects 'data' as a dictionary or DataFrame.
        """
        if isinstance(data, dict):
            self.data = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Data must be a dictionary or pandas DataFrame")

    def show_data(self):
        """Method to display the DataFrame."""
        print("Current DataFrame:")
        print(self.data)

    def add_column(self, col_name, values):
        """
        Adds a new column to the DataFrame.
        Raises an error if the length of the values doesn't match.
        """
        if len(values) != len(self.data):
            raise ValueError("The length of values must match the number of rows in the DataFrame.")
        self.data[col_name] = values

    def get_summary(self):
        """Returns a summary of the DataFrame."""
        return self.data.describe()

# Inherited class. (inherits from DataFrameProcessor, adding extra functionality)
class AdvancedDataFrameProcessor(DataFrameProcessor):
    def __init__(self, data):
        """Constructor that calls the base class constructor."""
        super().__init__(data)

    def normalize_columns(self):
        """
        Normalize numerical columns in the DataFrame.
        This method scales values between 0 and 1 for numerical columns.
        """
        numerical_columns = self.data.select_dtypes(include=np.number).columns
        self.data[numerical_columns] = (self.data[numerical_columns] - self.data[numerical_columns].min()) / (self.data[numerical_columns].max() - self.data[numerical_columns].min())

    def filter_rows(self, condition):
        """
        Filter rows based on a condition passed as a lambda function.
        The condition should operate on a row of the DataFrame.
        """
        return self.data[self.data.apply(condition, axis=1)]

# Example usage
if __name__ == "__main__":
    # Create a sample dataset
    data = {
        "A": np.random.randint(1, 10, size=5),
        "B": np.random.randint(20, 30, size=5),
        "C": ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    }

    # Initialize the base class processor
    base_processor = DataFrameProcessor(data)
    base_processor.show_data()

    # Add a new column
    base_processor.add_column("D", [100, 200, 300, 400, 500])
    print("\nAfter adding a new column 'D':")
    base_processor.show_data()

    # Get summary statistics
    print("\nSummary Statistics:")
    print(base_processor.get_summary())



    # Initialize the advanced class
    advanced_processor = AdvancedDataFrameProcessor(data)
    print("\nBefore Normalization:")
    advanced_processor.show_data()

    # Normalize the numerical columns
    advanced_processor.normalize_columns()
    print("\nAfter Normalization:")
    advanced_processor.show_data()

    # Filter rows with a custom condition (for example, filter rows where column A > 5)
    filtered_data = advanced_processor.filter_rows(lambda row: row["A"] > 0.5)
    print("\nFiltered Rows where A > 0.5:")
    print(filtered_data)