# Stock Market Dashboard Project Summary

## Objective
The primary objective of this project is to create a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Architecture and Tech Stack
The application is built using a multi-page architecture with the **Streamlit** framework.
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`). Pages include Home, Finance Dashboard, and Prediction, located in the `apps/` directory.
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts and technical indicators.
- **Forecasting / Machine Learning**: Utilizes Facebook's `Prophet` library for time-series stock price forecasting.
- **Deployment**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

## Key Features
- **Real-Time Market Data**: Live scraping of active trends and recent financial news.
- **Technical Analysis Dashboard**: Automatic calculation and interactive plotting of key indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index).
- **Time-Series Forecasting**: Users can predict future stock prices for a specified horizon (1 to 4 months) and visualize the forecast alongside raw data.
- **Scalable Multipage UI**: Easy navigation between different analytical views and models.

## Task List & Roadmap
- [ ] **Data Acquisition**: Sources for data - Yahoo Finance API, Stocktwit API.
- [ ] **EDA**: Understanding the features and data using various statistical methods like moving average, Hypothesis tests, Computing confidence Intervals for population data etc.
- [ ] **Data Visualization**:
  1. Box plots on opening and closing prices to show the spread of stock price on daily and monthly basis.
  2. Histograms and density plots to show the moving average or volatility in stock data.
  3. Density plots to show various features like price to earning ratio etc.
- [ ] **First web dashboard**: Base web application to show all the above results using Streamlit and deploy Heroku.
- [ ] **Machine Learning Problem Formulation**: Come up with the problem(s) or task(s) that we can solve using ML.
- [ ] **Preprocessing**: Dealing with volatility, Outliers, missing data, class imbalance, and Scaling data.
- [ ] **Model selection and Feature Engineering**: Select simple linear models to set a benchmark, check feature importance, experiment with new features.
- [ ] **Hyperparameter tuning and Validation**: Experiment with different models, tune hyperparameters, use ensembles like Bagging, Boosting (RF, GBDT) and Stacking, finalize the model.
- [ ] **Prediction on test data and performance check**: Predict on test and real-time data, check performance by using appropriate metric.
- [ ] **Prototype model deployment**: Deploying the full functioning prototype.
- [ ] **Scaling up the model**: Develop a sequence model (Deep Learning model, e.g. LSTMs) to achieve the same task, and perform Natural Language Inference (NLP) from current stock news by web scraping the news data and applying state-of-the-art techniques.
