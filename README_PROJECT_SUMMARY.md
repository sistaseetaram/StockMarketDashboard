# Project Objective & Summary

The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Summary

This real-time stock market dashboard is built using the **Streamlit** framework with a multi-page architecture.

### Key Features
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data. Sources for data also include Stocktwit API.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts, volume bars, and technical indicators. Features include:
  - Box plots on opening and closing prices to show the spread of stock price on daily and monthly basis.
  - Histograms and density plots to show the moving average or volatility in stock data.
  - Density plots to show various features like price to earning ratio etc.
- **Technical Analysis Dashboard**: Automatic calculation and interactive plotting of key indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index).
- **Time-Series Forecasting**: Users can predict future stock prices for a specified horizon (1 to 4 months) and visualize the forecast alongside raw data using Facebook's `Prophet` library for time-series forecasting.
- **Scalable Multipage UI**: Easy navigation between different analytical views and models, including Home, Finance Dashboard, and Prediction, located in the `apps/` directory.

### Architecture and Tech Stack
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`).
- **Deployment Ready**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

### Machine Learning Problem Formulation
- Here we will come up with the problem(s) or task(s) that we can solve using ML.
- **Preprocessing**: Dealing with volatility in data, Outliers and missing data, Imbalance in data, and Scaling data.
- **Model selection and Feature Engineering**: Selecting simple linear models to set a benchmark, checking feature importance, and experimenting with new features.
- **Hyperparameter tuning and Validation**: Experimenting with different models and tuning their hyperparameters. Experimenting with ensembles like Bagging, Boosting and Stacking techniques (RF, GBDT). Finalizing the model.
- **Prediction on test data and performance check**: Predicting results on test and real-time data, and checking performance using appropriate metrics.

### Future Work / Scaling Up
- Prototype model deployment: Deploying the full functioning prototype.
- Scale up the project by adding functionalities like:
  - Develop a sequence model (Deep Learning model, e.g., LSTM) to achieve the same task and check its performance.
  - Natural Language Inference from current stock news by web scraping the news data and then applying state-of-the-art NLP techniques.
