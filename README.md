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
## Results

### Daily Forecasting (Test: 2017–2018)
| Model          | MAE      | RMSE     | MAPE   |
|----------------|----------|----------|--------|
| Deterministic  | 62,017   | 88,148   | 11.9%  |
| Hybrid         | 50,408   | 72,744   | 10.8%  |
| Naïve-1D       | 47,952   | 71,578   | 10.7%  |
| Naïve-7D       | 79,265   | 110,389  | 14.5%  |

**Hybrid improved over deterministic by ~20%**, though naïve-1D remained a strong benchmark.

---

### Monthly Forecasting (Test: 2011–2018)
| Model          | MAE       | RMSE      | MAPE   |
|----------------|-----------|-----------|--------|
| Deterministic  | ~1.86e6   | ~3.01e6   | 18.9% |
| Hybrid         | ~1.97e6   | ~3.13e6   | 19.1% |
| Naïve-1M       | ~2.70e6    | ~3.91e6    | 26.0%   |
| Naïve-7M       | ~2.84e6    | ~4.18e6    | 26.1%   |

Performance is reasonable without weather/economic covariates, showing the pipeline’s flexibility across granularities.

---

## Key Features
- **Reusable pipeline**:
  - `make_deterministic_features()` – builds trend + Fourier seasonal features.
  - `make_residual_features()` – constructs lag, rolling, and calendar features.

- **Hybrid Model Design**:
  - Linear Regression captures global structure (trend, seasonality).
  - XGBoost learns nonlinear residual patterns.
  - Final forecast = deterministic + residual corrections.

- **Robust Evaluation**:
  - Compared against naïve baselines.
  - Metrics: MAE, RMSE, MAPE (with caution for small denominators).
  - Visualization of forecasts vs. actual demand.

## Key Takeaways
- Demonstrated ability to engineer **time-series features** (lags, rolling windows, Fourier terms).
- Built a **hybrid ML pipeline** (deterministic + boosted residuals) usable at multiple temporal resolutions.
- Achieved **10–11% MAPE at daily level** and **18% MAPE at monthly level**, competitive given the lack of exogenous drivers.
- Reinforced the importance of **strong naïve baselines** in time series evaluation.

---

## Next Steps
- Add **temperature/weather covariates** (e.g., NOAA datasets).
- Explore **stacked hybrids** (combine multiple base models).
- Extend to **multi-step forecasting** (beyond one horizon).
- **Hyperparamater tuning** for XGBOOST
- Package as a reusable Python module for load forecasting.
