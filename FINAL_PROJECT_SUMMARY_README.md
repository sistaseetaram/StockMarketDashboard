# Project Objective & Summary

## Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application.

## Summary
This project is a multipage web application built with Streamlit. It fetches data via the `yfinance` API, scrapes financial news and top market movers using `BeautifulSoup`, and generates interactive charts with `Plotly`. It includes time-series forecasting utilizing Facebook's `Prophet` library to predict future stock prices up to 4 months in advance.

## Key Features
- **Data Acquisition**: Fetch real-time and historical stock data.
- **Web Scraping**: Extract financial news and market movers.
- **Data Visualization**: Responsive candlestick charts, volume bars, and technical indicators using `Plotly`.
- **Technical Analysis**: Automatic calculation of indicators like MACD and RSI.
- **Forecasting**: Predicting future prices with `Prophet`.
- **Scalable UI**: A multi-page layout (Home, Finance Dashboard, Prediction) leveraging Streamlit.

## Tech Stack
- **Frontend/Framework**: Streamlit
- **Data Acquisition**: yfinance, BeautifulSoup
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Plotly
- **Machine Learning**: Prophet
- **Deployment**: Configured for Heroku (Procfile, setup.sh)
