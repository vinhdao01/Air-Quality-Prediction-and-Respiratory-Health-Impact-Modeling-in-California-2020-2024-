# data_preprocessing.py

# PURPOSE:
# Load, inspect, and clean datasets for analysis and modeling

import pandas as pd


def load_data(filepath):
    """
    Load a CSV file into a DataFrame
    """
    return pd.read_csv(filepath)


def inspect_data(df, name="dataset"):
    """
    Print basic information about a dataset
    """
    print(f"\n{name}")
    print("Columns:", df.columns.tolist())
    print(df.head(2))


def load_multiple_datasets(file_list):
    """
    Load multiple datasets into a dictionary
    """
    data_dict = {}

    for file in file_list:
        try:
            df = pd.read_csv(file)
            data_dict[file] = df
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return data_dict


def inspect_multiple_datasets(file_list):
    """
    Load and inspect multiple datasets
    """
    for file in file_list:
        try:
            df = pd.read_csv(file)
            inspect_data(df, file)
        except Exception as e:
            print(f"\nERROR reading {file}: {e}")


def clean_column_names(df):
    """
    Standardize column names
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
