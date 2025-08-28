# Energy Consumption Forecasting with Hybrid Time Series Models *(In Progress)*

## Project Overview  
This project focuses on **forecasting daily electricity demand** using the PJM regional energy dataset (~15 years of hourly data). The goal is to design a **comprehensive and reproducible forecasting workflow** that combines classical time series decomposition with modern machine learning.  

By integrating **deterministic trend/seasonality models** with **residual learning via XGBoost**, the project aims to produce forecasts that outperform naïve and seasonal persistence baselines, while remaining interpretable and extensible.  

---

## Key Features (Completed So Far)  
- **Data ingestion & aggregation**  
  - Loaded PJM hourly electricity demand data.  
  - Aggregated to daily granularity for forecasting.  
  - Persisted clean datasets in versioned folders (`data/raw`, `data/interim`, `data/processed`).  

- **Exploratory time series analysis (EDA)**  
  - Identified clear daily/weekly/annual seasonal patterns.  
  - Performed moving average trend analysis and seasonal decomposition.  
  - Autocorrelation, partial autocorrelation, and lag plots to uncover serial dependence.  

- **Deterministic modeling**  
  - Fitted polynomial trend + Fourier seasonal terms using `DeterministicProcess`.  
  - Generated baseline forecasts for test window.  
  - Extracted residuals as detrended, deseasonalized signals.  

- **Residual feature design**  
  - Built lagged, rolling mean/std features.  
  - Incorporated calendar features (day-of-week, month, weekend flag).  
  - Integrated U.S. holiday effects into the dataset.  

---

## Next Steps  
- Train and evaluate **hybrid models** (XGBoost and Ridge regression) on residuals.  
- Benchmark performance against naïve and seasonal persistence forecasts.  
- Extend pipeline to **weekly and monthly horizons**.  
- Experiment with **stacked/ensemble hybrids** (e.g., ARIMA + XGBoost).  
- Deploy the pipeline for **automated reproducible forecasting**.  
