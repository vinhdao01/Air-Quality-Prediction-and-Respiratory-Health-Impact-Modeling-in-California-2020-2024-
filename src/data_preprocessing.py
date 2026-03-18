import pandas as pd

# =========================
# Load Data
# =========================
def load_data(file_path):
    """
    Load CSV file into pandas DataFrame
    """
    return pd.read_csv(file_path)


# =========================
# Standardize Columns
# =========================
def standardize_columns(df):
    """
    Convert column names to lowercase and replace spaces with underscores
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# =========================
# Parse Dates
# =========================
def parse_dates(df):
    """
    Convert 'weekend' column to datetime if it exists
    """
    if "weekend" in df.columns:
        df["weekend"] = pd.to_datetime(df["weekend"])
    return df


# =========================
# Create Lag Features
# =========================
def create_lag_features(df, column, lags=[1, 2, 3]):
    """
    Create lagged features for time series modeling
    """
    for lag in lags:
        df[f"{column}_lag{lag}"] = df[column].shift(lag)
    return df


# =========================
# Basic Data Check
# =========================
def check_data(files):
    """
    Print columns and preview for all datasets
    """
    for f in files:
        try:
            df = pd.read_csv(f)
            print(f"\n{f}")
            print(df.columns.tolist())
            print(df.head(2))
        except Exception as e:
            print(f"\nERROR reading {f}: {e}")
