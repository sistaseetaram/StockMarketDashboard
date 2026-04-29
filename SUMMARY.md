# Stock Market Dashboard Project Summary

## Objective
The objective of this project is to create a real-time stock market dashboard. It provides an interactive web application to visualize technical indicators, price information, and forecasts for selected stock tickers using data retrieved from Yahoo Finance and other sources.

## Architecture
The application is built using the Streamlit framework, following a multi-page architecture.
- **Main Entry Point (`app.py`)**: Initializes a `MultiApp` instance and registers the individual pages (Home, Finance Dashboard, Prediction) to route users through the application.
- **Pages (`apps/` directory)**:
  - **`home.py`**: The landing page that displays the latest trends (Most Active, Gainers, Losers) by web scraping Yahoo Finance, and displays the latest finance news by web scraping Google News.
  - **`financeDashboard.py`**: A detailed dashboard for a selected stock ticker (e.g., GOOG, MSFT, S&P 500, NIFTY 50). It fetches historical data using `yfinance` and plots interactive candlestick charts along with technical indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index) using Plotly.
  - **`prediction.py`**: A forecasting page that allows users to predict future stock prices for a selected ticker over a specified number of months (1 to 4). It utilizes the Facebook Prophet library (`fbprophet`) for time-series forecasting and plots the raw data and forecast using Plotly.

## Current Features
- **Data Acquisition**: Real-time and historical stock data retrieval using `yfinance` API.
- **Web Scraping**: Extraction of top gainers, losers, and most active stocks from Yahoo Finance, and latest finance news from Google News using `BeautifulSoup`.
- **Data Visualization**: Interactive and responsive candlestick charts, volume bars, MACD, and RSI plots using Plotly `graph_objects` and `subplots`.
- **Technical Indicators**: Automated calculation and plotting of EMAs, MACD, Signal, Histogram, and RSI.
- **Forecasting**: Time-series forecasting of stock prices using Facebook Prophet, allowing user-defined prediction horizons.
- **Deployment Ready**: The repository includes `Procfile`, `setup.sh`, and `runtime.txt`, indicating it is configured for deployment on platforms like Heroku.
