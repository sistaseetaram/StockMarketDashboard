# Project Objective Summary

The main objective of this repository is to create a comprehensive, real-time **Stock Market Dashboard** using the Streamlit framework. This interactive application provides insights into financial markets by combining data acquisition, exploratory data analysis (EDA), visualization, and machine learning prediction.

## Key Features

### 1. Data Acquisition
* Data is fetched dynamically from Yahoo Finance via the `yfinance` API and web scraping techniques (using `BeautifulSoup` and `requests`).
* The system gathers historical stock data as well as real-time market trends such as Top Gainers, Losers, and Most Active stocks.
* Latest finance news is also scraped and presented directly within the dashboard.

### 2. Exploratory Data Analysis (EDA) & Data Visualization
* **Financial Dashboard:** A dedicated interactive page (using Plotly) visualizing vital technical indicators:
  * **Candlestick Charts:** For opening, closing, high, and low price visualization.
  * **Moving Averages:** 12-period and 26-period Exponential Moving Averages (EMAs).
  * **MACD:** Moving Average Convergence Divergence with signal lines and histograms to spot price momentum.
  * **RSI:** Relative Strength Index to identify overbought and oversold conditions.
  * **Volume:** Bar charts displaying daily trading volume.

### 3. Machine Learning & Forecasting
* **Stock Price Prediction:** Leveraging Facebook's `fbprophet` library (via time-series forecasting models), the application is capable of projecting future stock prices.
* Users can specify prediction windows to visualize upcoming market trends, extending the dashboard's capabilities from mere historical analysis to predictive insights.

## Conclusion
This repository serves as an end-to-end prototype mapping the journey from raw stock data acquisition and pre-processing to advanced technical visualizations and time-series prediction models, all wrapped within an interactive, user-friendly web application deployable on platforms like Heroku.