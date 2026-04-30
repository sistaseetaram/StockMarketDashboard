# Project Summary

## Objective
The primary objective of this project is to create a real-time stock market dashboard. It serves as an end-to-end data science and machine learning web application that allows users to analyze stock data, perform technical analysis, and predict future stock prices.

## Key Phases & Tasks
Based on the project's roadmap, the development lifecycle covers several key areas:

1. **Data Acquisition & EDA**:
   - Acquiring data from sources like Yahoo Finance API and Stocktwit API.
   - Understanding features and data via statistical methods (moving averages, hypothesis testing, confidence intervals).

2. **Data Visualization & Base Dashboard**:
   - Creating box plots, histograms, and density plots to illustrate stock price spreads, volatility, and features like price-to-earning ratios.
   - Building the first web dashboard with all insights using Streamlit and deploying it to Heroku.

3. **Machine Learning Pipeline**:
   - Problem formulation and data preprocessing (dealing with volatility, outliers, missing data, imbalance, and scaling).
   - Model selection and feature engineering, starting with simple linear models as benchmarks.
   - Hyperparameter tuning, validation, and experimenting with ensemble methods (Bagging, Boosting, Stacking like RF, GBDT).

4. **Forecasting & Deployment**:
   - Predicting results on test and real-time data and checking performance using appropriate metrics.
   - Deploying the fully functioning prototype model.

5. **Scaling Up**:
   - Adding sequence models (Deep Learning, e.g., LSTMs) for time-series forecasting.
   - Implementing Natural Language Inference using state-of-the-art NLP techniques on scraped financial news data.

## Architecture
The application is structured as a multi-page Streamlit web app:
- **Home Page**: Displays current market trends (Most Active, Gainers, Losers) and recent financial news by scraping data.
- **Finance Dashboard**: Provides interactive candlestick charts and technical indicators (MACD, RSI) using Plotly and data from `yfinance`.
- **Prediction Page**: Allows users to forecast future stock prices using time-series models like Facebook Prophet.
