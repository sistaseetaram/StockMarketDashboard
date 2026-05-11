# Stock Market Dashboard Project Summary

## Objective
The main objective of this project is to create a real-time stock market dashboard. It offers an interactive web application that allows users to visualize technical indicators, monitor price information, check latest trends and news, and forecast future stock prices for selected tickers.

## Architecture
The application is built using the Streamlit framework and follows a multi-page architecture to separate concerns and provide a clean user interface.

- **Main Entry Point (`app.py`)**: Initializes a `MultiApp` instance to handle routing across the different application pages (Home, Finance Dashboard, Prediction).
- **Pages (`apps/` directory)**:
  - **`home.py`**: The landing page that displays the latest market trends (Most Active, Gainers, Losers) by dynamically scraping Yahoo Finance using `BeautifulSoup`. It also aggregates and displays the latest finance news by web scraping Google News.
  - **`financeDashboard.py`**: A detailed dashboard for an individual stock ticker (e.g., GOOG, AAPL, MSFT). It fetches historical data (from 2015 to present) using `yfinance` and plots interactive financial charts using Plotly. Features include candlestick charts, volume bars, and technical indicators such as Moving Average Convergence Divergence (MACD) and Relative Strength Index (RSI).
  - **`prediction.py`**: A forecasting tool that predicts future stock prices. Users can select a forecast horizon (between 1 to 4 months). It leverages the Facebook Prophet library (`fbprophet`) for time-series forecasting and visualizations to plot the raw data and predicted future trends.
  - **`utils.py`**: Houses shared utility functions, such as `get_ticker_selection`, to ensure consistency across the different pages.

## Key Features
- **Data Acquisition**: Integration with `yfinance` to retrieve historical and real-time stock data.
- **Web Scraping**: Custom scraping logic using `BeautifulSoup` to extract actionable market trends from Yahoo Finance and top news from Google News.
- **Interactive Visualization**: Utilization of Plotly (`graph_objects` and `subplots`) to render responsive and highly customizable financial charts (candlestick, MACD, RSI, volume).
- **Technical Indicators**: Automated computation of Exponential Moving Averages (EMA12, EMA26), MACD (Signal and Histogram), and RSI.
- **Forecasting (Machine Learning)**: Time-series forecasting of stock prices using Facebook Prophet.
- **Deployment Ready**: The project includes necessary configurations (`Procfile`, `setup.sh`, `runtime.txt`) for cloud deployment platforms such as Heroku.
