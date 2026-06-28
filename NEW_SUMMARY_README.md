# Stock Market Dashboard Summary

## Project Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Summary
This real-time stock market dashboard is built using the **Streamlit** framework with a multi-page architecture.

### Key Features & Task List Summary
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data. Extracts top market movers and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Exploratory Data Analysis (EDA)**: Understand features and data using statistical methods, moving average, hypothesis tests, etc.
- **Data Visualization**: Leverages `Plotly` for responsive candlestick charts, volume bars, histograms, and density plots to show the moving average, volatility, and various features.
- **First Web Dashboard**: Base web application showing insights using Streamlit, deployed to Heroku. Automatic calculation and interactive plotting of key technical indicators like MACD and RSI.
- **Machine Learning Problem Formulation**: Formulating problems to solve using ML.
- **Preprocessing**: Dealing with data volatility, outliers, missing data, class imbalance, and data scaling.
- **Model Selection & Feature Engineering**: Selecting linear models for benchmarks, checking feature importance, experimenting, and finalizing features.
- **Time-Series Forecasting / Tuning**: Users can predict future stock prices for a specified horizon (1 to 4 months) using Facebook's `Prophet` library. Experimenting with different models, tuning hyperparameters, and using ensembles (Bagging, Boosting, Stacking like RF, GBDT).
- **Prediction & Performance Check**: Predicting results on test and real-time data, checking performance with appropriate metrics.
- **Prototype Model Deployment**: Deploying the full functioning prototype.
- **Future Work / Scaling Up**: Adding functionalities like deep learning sequence models (LSTM) and applying state-of-the-art NLP techniques to Natural Language Inference from current stock news.

### Architecture and Tech Stack
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`).
- **Deployment Ready**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.
