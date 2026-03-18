import matplotlib.pyplot as plt


# =========================
# AQI Trend Plot
# =========================
def plot_aqi_trend(df):
    plt.figure()
    plt.plot(df["weekend"], df["popweighted_aqi"])
    plt.title("Statewide AQI Over Time")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/eda_trends.png")
    plt.close()


# =========================
# Forecast Plot
# =========================
def plot_forecast(df):
    plt.figure()
    plt.plot(df["WeekEnd"], df["Actual"], label="Actual")
    plt.plot(df["WeekEnd"], df["SARIMA_Forecast"], label="SARIMA Forecast")
    plt.legend()
    plt.title("AQI Forecast vs Actual")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/forecast_plot.png")
    plt.close()


# =========================
# Model Performance Plot
# =========================
def plot_model_performance(df):
    df.plot(x="Model", y=["MAE", "RMSE"], kind="bar")
    plt.title("Model Performance Comparison")
    plt.tight_layout()
    plt.savefig("images/model_performance.png")
    plt.close()
