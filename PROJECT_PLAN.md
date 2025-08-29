# Energy Forecasting (PJME Daily Load)

## Overview
Forecast total daily electricity consumption for the **PJM Eastern Region (PJME)** using classical time series methods and machine learning models.  
The goal is to predict **7 days ahead** and compare statistical and machine learning approaches against a **seasonal naïve baseline**.

---

## Data
- **Source:** [Kaggle PJM Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)  
- **File used:** `PJME_hourly.csv`  
- **Span:** 2002-01-01 → 2018-08-03  
- **Granularity:** Hourly → aggregated to **daily total (sum)**

---

## EDA Completed
- Basic stats, full-series and zoomed plots.  
- Seasonal decomposition (annual cycle).  
- Calendar features: average by weekday & month.  
- Autocorrelation analysis: ACF, PACF, lag plots (1–10).  
- Figures saved in `reports/figures/`.

---

## 3. Feature Engineering
- **Calendar Features:** Day-of-week, weekend flag, month-of-year, holiday indicators (daily only).
- **Lag Features:**  
  - Daily: `[1,2,7,14,21,28]`.  
  - Monthly: `[1,2,3,6,12]`.
- **Rolling Features:**  
  - Daily: `[7,14,28]` days.  
  - Monthly: `[3,6,12]` months.
- **Deterministic + Fourier:** Linear trend + annual/weekly Fourier terms.

---

## 4. Modeling
- **Deterministic Model:** Linear Regression fit on deterministic features (trend + Fourier).
- **Hybrid Model:** XGBoost fit on residuals, combined with deterministic baseline.
- **Baselines:** Naïve-1D, Naïve-7D, Naïve-1M, Naïve-7M for comparison.

---

## 5. Evaluation
- **Metrics:** MAE, RMSE, MAPE.

---

## 6. Next Steps
- Incorporate external covariates (temperature, population).
- Expand hybrid models (stacked ensembles).
- Extend to probabilistic forecasting (prediction intervals).
- Package pipeline for flexible re-use at any temporal granularity.

---

