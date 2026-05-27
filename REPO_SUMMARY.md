# Real-time Stock Market Dashboard

## Project Objective
The objective of this project is to create an interactive, real-time stock market dashboard. The application is built using Streamlit and visualizes technical indicators and price information for selected tickers. It integrates data from Yahoo! Finance and Google News to provide comprehensive insights, trend analysis, and stock forecasting.

## Architecture and Framework
The project uses a multipage Streamlit framework (`multiapp.py`) to organize its features into distinct pages:
- **Home**: A dashboard home page that provides the latest market trends (Most Active, Gainers, Losers) scraped from Yahoo! Finance and displays the top 5 latest finance news headlines scraped from Google News.
- **Finance Dashboard**: An interactive visualization page that displays historical stock data (candlestick charts) and technical indicators such as Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), and trading volume using Plotly.
- **Prediction**: A stock forecasting app that uses Facebook's Prophet machine learning model to predict future stock prices (up to 4 months) based on historical closing prices.

## Data Acquisition and Libraries
- **Data Sources**: Yahoo! Finance API (`yfinance`), Google News, and Yahoo! Finance web scraping.
- **Key Libraries**:
  - `streamlit` for the interactive web interface.
  - `pandas` and `numpy` for data manipulation.
  - `plotly` for creating interactive financial charts.
  - `requests` and `bs4` (BeautifulSoup) for web scraping.
  - `fbprophet` for time series forecasting.

## Key Features
- **Real-Time Data Extraction**: Web scraping the latest top trends and news.
- **Technical Indicators**: Automated calculation and plotting of MACD, Signal lines, RSI, and moving averages (EMA12, EMA26).
- **Interactive Visualizations**: Multi-plot charts providing zoom, pan, and hover capabilities over historical stock data.
- **Machine Learning**: Time-series forecasting to predict future stock behavior.
