# Data Dictionary

This document describes datasets used in the Air Quality and Respiratory Health Modeling project.

---

## 📊 weekly_statewide_aqi.csv

**Description:** Weekly population-weighted AQI across California.

| Column | Description |
|--------|------------|
| WeekEnd | End date of the week |
| PopWeighted_AQI | Population-weighted AQI |

---

## 📊 weekly_county_aqi.csv

**Description:** Weekly AQI by county.

| Column | Description |
|--------|------------|
| WeekEnd | Week ending date |
| County | County name |
| Mean_AQI | Average AQI |

---

## 📊 annual_county_aqi.csv

**Description:** Annual AQI by county.

| Column | Description |
|--------|------------|
| COUNTY | County name |
| Year | Year |
| Mean_AQI | Average AQI |

---

## 📊 joint_aqi_health_county.csv

**Description:** Combined dataset of AQI and health outcomes.

| Column | Description |
|--------|------------|
| COUNTY | County name |
| Year | Year |
| Mean_AQI | Average AQI |
| County_join | Join key |
| NUMBER OF HOSPITALIZATIONS | Asthma hospitalizations |
| AGE-ADJUSTED HOSPITALIZATION RATE | Rate per population |
| NUMBER OF ED VISITS | Emergency visits |
| AGE-ADJUSTED ED VISIT RATE | Rate per population |

---

## 📊 asthma_ed_clean.csv / asthma_hosp_clean.csv

**Description:** Cleaned health datasets.

| Column | Description |
|--------|------------|
| COUNTY | County |
| YEAR | Year |
| AGE GROUP | Age group |
| NUMBER OF ED VISITS | ED visits |
| NUMBER OF HOSPITALIZATIONS | Hospitalizations |

---

## 📊 aqi_model_metrics.csv

| Column | Description |
|--------|------------|
| Model | Model name |
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |

---

## 📊 aqi_forecast_results.csv

| Column | Description |
|--------|------------|
| WeekEnd | Forecast date |
| Actual | Actual AQI |
| ARIMA_Forecast | ARIMA prediction |
| SARIMA_Forecast | SARIMA prediction |
| RandomForest | RF prediction |

---

## 📊 health_model_metrics.csv

| Column | Description |
|--------|------------|
| Model | Model name |
| R2 | R-squared |
| MAE | Error |
| RMSE | Error |

---

## 📊 health_model_predictions.csv

| Column | Description |
|--------|------------|
| Mean_AQI | AQI value |
| AQI_lag1 | Lagged AQI |
| Actual | Actual outcome |
| Pred_LR | Linear Regression prediction |
| Pred_RF | Random Forest prediction |
| Pred_GB | Gradient Boosting prediction |
