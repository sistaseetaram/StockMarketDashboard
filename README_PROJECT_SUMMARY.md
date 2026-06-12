# Project Summary: StockMarketDashboard

## Objective
The objective of this project is to create a real-time stock market dashboard.

## Project Architecture
This project is built as a multi-page web application using **Streamlit** (v1.8.1) and is configured for deployment on **Heroku**.
The main entry point is `app.py` inside the `finaltest2` folder, which routes to different pages (Home, Finance Dashboard, Prediction) through `multiapp.py`.

## Key Features & Task Overview
- **Data Acquisition**: Scraping and fetching data using APIs like Yahoo Finance and StockTwit.
- **Exploratory Data Analysis (EDA)**: Statistical analysis including moving averages, hypothesis tests, and confidence intervals.
- **Data Visualization**: Box plots, histograms, and density plots to illustrate stock volatility, moving averages, and metrics like P/E ratios.
- **Machine Learning & Predictions**:
  - Problem formulation, preprocessing (handling volatility, outliers, missing data, imbalances, scaling).
  - Feature engineering and model selection starting with linear models and advancing to ensemble techniques (Random Forest, GBDT).
  - Hyperparameter tuning, validation, and real-time predictions.
- **Future Scaling**: Plans to incorporate Deep Learning (Sequence Models/LSTM) and Natural Language Inference from real-time stock news.
