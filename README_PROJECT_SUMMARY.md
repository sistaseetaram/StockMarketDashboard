# Project Objective

The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

# Task Checklist

- [ ] Data Acquisition.
  1. Sources for data - Yahoo Finance API, Stocktwit API.
- [ ] EDA
  1. Understanding the features and data using various statistical methods like <br/> moving average, Hypothesis tests, Computing confidence Intervals for population data etc.
- [ ] Data Vizualization
  1. Box plots on opening and closing prices to show the spread of stock price on daily and monthly basis.
  2. Histograms and density plots to show the moving average or volatility in stock data.
  3. Density plots to show various features like price to earning ratio etc.
- [ ] First web dashboard with all the insights.
  1. Base web application to show all the above results using SreamLit and deploy Heroku.
- [ ] Machine Learning Problem Formulation.
  1. Here we will come up with the problem(s) or task(s) that we can solve using ML.
- [ ] Preprcessing
  1. Dealing with volatility in data.
  2. Dealing with Outliers and missing data.
  3. Dealing with Imabalance in data.
  4. Scaling data.
- [ ] Model selection and Feature Engineering
  1. First, we select some simple linear models to set a benchmark for future model selection.
  2. Then check the feature importance and add more features by feature.
  3. And then experiment with the new features and decide the final set of features.
- [ ] Hyperparameter tuning and Validation and finalizing the model.
  1. Now, Experiment with different models and tune their respective hyperparameters.
  2. Experiment with ensembles like Bagging, Boosting and Stacking techniques.(RF,GBDT)
  3. Finalize the model.
- [ ] Prediction on test data and performance check.
  1. Predict the resultsont test and real time data.
  2. Check performance by using appropriate metric.
- [ ] Prototype model deployment.
  1. Deploying the full functioning prototype.
- [ ] Scaling up the model by adding more features and data.
  1. Scale up the project by adding functionalities like
      1. Develop a sequence model(Deep Learning model) to achive the same task and check its performance.
      2. Natural Language Inference from current stock news by web scrapping the news data and then applying LSTM's and other state of the art techniques.

# Summary

This real-time stock market dashboard is built using the **Streamlit** framework with a multi-page architecture.

## Key Features
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts, volume bars, and technical indicators.
- **Technical Analysis Dashboard**: Automatic calculation and interactive plotting of key indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index).
- **Time-Series Forecasting**: Users can predict future stock prices for a specified horizon (1 to 4 months) and visualize the forecast alongside raw data using Facebook's `Prophet` library for time-series forecasting.
- **Scalable Multipage UI**: Easy navigation between different analytical views and models, including Home, Finance Dashboard, and Prediction, located in the `apps/` directory.

## Architecture and Tech Stack
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`).
- **Deployment Ready**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

## Future Work
- Scale up the project by adding functionalities like deep learning sequence models (LSTM) to achieve the same task and check performance.
- Perform Natural Language Inference from current stock news by web scraping the news data and applying state-of-the-art NLP techniques.
- Improve handling of data volatility, outliers, missing data, and class imbalance.
