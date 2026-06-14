# Real-Time Stock Market Dashboard Summary

## Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Architecture and Tech Stack
The application is built using a multi-page architecture with the **Streamlit** framework.
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`). Pages include Home, Finance Dashboard, and Prediction, located in the `apps/` directory.
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts and technical indicators.
- **Forecasting / Machine Learning**: Utilizes Facebook's `Prophet` library for time-series stock price forecasting.
- **Deployment**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

## Task List & Summary
1. **Data Acquisition:** Sourcing data from Yahoo Finance API and Stocktwit API.
2. **Exploratory Data Analysis (EDA):** Understanding features through moving averages, hypothesis testing, and confidence intervals.
3. **Data Visualization:** Creating box plots, histograms, and density plots to show stock price spread, moving average/volatility, and various features like price to earning ratio.
4. **First Web Dashboard:** Building the base web application to display insights using StreamLit and deploying to Heroku.
5. **Machine Learning Problem Formulation:** Defining tasks that can be solved using ML.
6. **Preprocessing:** Handling data volatility, outliers, missing data, imbalanced data, and scaling.
7. **Model Selection & Feature Engineering:** Benchmarking with simple linear models, checking feature importance, and experimenting with new features to finalize the set.
8. **Hyperparameter Tuning & Validation:** Experimenting with various models, tuning hyperparameters, and testing ensembles like Bagging, Boosting, and Stacking (RF, GBDT).
9. **Prediction & Performance Check:** Predicting results on test and real-time data, and evaluating performance using appropriate metrics.
10. **Prototype Model Deployment:** Deploying the fully functional prototype.
11. **Scaling Up:** Enhancing the project by developing a sequence model (Deep Learning) and applying Natural Language Inference to scraped stock news data using LSTMs and other state-of-the-art techniques.
