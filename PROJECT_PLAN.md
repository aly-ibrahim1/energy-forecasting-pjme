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

