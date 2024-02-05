import pandas as pd

def read_csv_to_dataframe(csv_file_path, delimiter=','):
    """
    Reads a CSV file into a pandas DataFrame.

    Args:
        csv_file_path (str): The file path to the CSV file.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.

    Returns:
        DataFrame: A pandas DataFrame containing the data from the CSV file.

    Example:
        >>> df = read_csv_to_dataframe('/path/to/file.csv')
        >>> print(df.head())  # Print the first few rows of the DataFrame
    """
    try:
        # Use pandas to read the CSV file
        dataframe = pd.read_csv(csv_file_path, delimiter=delimiter)
        return dataframe
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

# Example usage:
# df = read_csv_to_dataframe('your_file.csv')
# print(df)