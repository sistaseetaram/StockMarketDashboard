# Stock Market Dashboard Project Summary

## Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Summary
The application is built using the **Streamlit** framework with a multi-page architecture.

### Architecture and Tech Stack
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`). The pages include Home, Finance Dashboard, and Prediction, located in the `apps/` directory.
- **Data Acquisition**: Utilizes the `yfinance` API for retrieving real-time and historical stock data.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts, volume bars, and technical indicators.
- **Technical Analysis**: Automatic calculation and interactive plotting of key indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index).
- **Forecasting / Machine Learning**: Utilizes Facebook's `Prophet` library for time-series stock price forecasting, allowing users to predict future stock prices for a specified horizon (1 to 4 months) and visualize the forecast alongside raw data.
- **Deployment**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

### Future Work
- Scale up the project by adding functionalities like deep learning sequence models (LSTM) to achieve the same task and check performance.
- Perform Natural Language Inference from current stock news by web scraping the news data and applying state-of-the-art NLP techniques to assess market sentiment.
- Improve handling of data volatility, outliers, missing data, and class imbalance.
- Implement advanced Machine Learning models, such as ensembles like Random Forests (RF), Gradient Boosting Decision Trees (GBDT), and stacking techniques.