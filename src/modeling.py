import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =========================
# Train/Test Split
# =========================
def split_data(df, target_column, test_size=0.2):
    """
    Split dataset into training and testing sets
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return train_test_split(X, y, test_size=test_size, random_state=42)


# =========================
# Evaluate Model
# =========================
def evaluate_model(y_true, y_pred):
    """
    Calculate MAE, RMSE, and R2
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred) ** 0.5
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


# =========================
# Save Metrics
# =========================
def save_metrics(metrics_dict, filename):
    """
    Save model metrics to CSV
    """
    df = pd.DataFrame(metrics_dict)
    df.to_csv(filename, index=False)


# =========================
# Save Predictions
# =========================
def save_predictions(df, filename):
    """
    Save predictions DataFrame
    """
    df.to_csv(filename, index=False)
