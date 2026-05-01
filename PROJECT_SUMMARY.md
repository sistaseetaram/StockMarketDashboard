# Stock Market Dashboard Project Summary

## Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts for selected stock tickers using data retrieved from Yahoo Finance and other sources. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Architecture
The application is built using a multi-page architecture with the **Streamlit** framework.
- **Main Entry Point (`app.py`)**: Initializes a `MultiApp` instance and registers the individual pages (Home, Finance Dashboard, Prediction) to route users through the application.
- **Pages (`apps/` directory)**:
  - **`home.py`**: The landing page that displays the latest trends (Most Active, Gainers, Losers) by web scraping Yahoo Finance, and displays the latest finance news by web scraping Google News.
  - **`financeDashboard.py`**: A detailed dashboard for a selected stock ticker (e.g., GOOG, MSFT, S&P 500, NIFTY 50). It fetches historical data using `yfinance` and plots interactive candlestick charts along with technical indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index) using Plotly.
  - **`prediction.py`**: A forecasting page that allows users to predict future stock prices for a selected ticker over a specified number of months (1 to 4). It utilizes the Facebook Prophet library (`fbprophet`) for time-series forecasting and plots the raw data and forecast using Plotly.

## Tech Stack
- **Frontend & Routing**: Streamlit, custom multi-page framework (`multiapp.py`).
- **Data Acquisition**: `yfinance` API, `requests`.
- **Web Scraping**: `BeautifulSoup` (bs4) for extracting top market movers and financial news.
- **Data Visualization**: `Plotly` (`graph_objects` and `subplots`), `matplotlib`.
- **Data Manipulation**: `pandas`, `numpy`.
- **Forecasting / Machine Learning**: Facebook's `Prophet` library for time-series stock price forecasting.
- **Deployment**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

## Key Features
- **Data Acquisition**: Real-time and historical stock data retrieval using `yfinance` API.
- **Web Scraping**: Real-time extraction of top gainers, losers, and most active stocks from Yahoo Finance, and latest finance news from Google News.
- **Data Visualization**: Interactive and responsive candlestick charts, volume bars, MACD, and RSI plots using Plotly.
- **Technical Indicators**: Automated calculation and interactive plotting of EMAs, MACD, Signal, Histogram, and RSI.
- **Forecasting**: Time-series forecasting of stock prices using Facebook Prophet, allowing users to predict future prices for a specified horizon (1 to 4 months).
- **Scalable Multipage UI**: Easy navigation between different analytical views and models.

## Future Roadmap (Planned Tasks)
- **Advanced Machine Learning**: Implement ensembles like Random Forests (RF), Gradient Boosting Decision Trees (GBDT), and stacking techniques.
- **Deep Learning Scale-Up**: Develop sequence models (e.g., LSTMs) to forecast prices and analyze performance against benchmark models.
- **Natural Language Processing (NLP)**: Perform Natural Language Inference on scraped stock news using state-of-the-art NLP techniques to assess market sentiment.
- **Enhanced Preprocessing**: Better handle data volatility, outliers, missing data, and class imbalance.
