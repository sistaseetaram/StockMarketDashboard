# StockMarketDashboard - Summary

## Objective
The primary objective of this project is to create a real-time stock market dashboard. It is an interactive web application that helps users analyze stock data, view technical indicators, perform exploratory data analysis, formulate machine learning problems, and view stock predictions.

## Key Features
- **Data Acquisition**: Scrapes financial data from sources like the Yahoo Finance API and Stocktwit API.
- **Exploratory Data Analysis (EDA)**: Understand features using statistical methods like moving averages, hypothesis tests, and confidence intervals.
- **Data Visualization**: Visualize opening/closing prices with box plots, stock volatility with histograms/density plots, and PE ratios with density plots.
- **Interactive Web Dashboard**: The application is built using Streamlit with a multi-page layout (Home, Finance Dashboard, Prediction) and deployed on Heroku.
- **Machine Learning Integration**: Formulation of ML tasks, comprehensive data preprocessing (handling volatility, outliers, missing data, imbalance, and scaling), model selection (simple linear models to ensembles like Random Forest and GBDT), feature engineering, hyperparameter tuning, and performance evaluation.
- **Scalability**: Plans for sequence models (Deep Learning) and Natural Language Inference from real-time stock news using LSTM and state-of-the-art NLP techniques.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For the interactive web dashboard.
- **Pandas, NumPy**: For data manipulation and analysis.
- **Plotly, Matplotlib**: For interactive and static data visualizations.
- **yfinance, Requests, BeautifulSoup4**: For financial data acquisition and web scraping.
- **fbprophet (Prophet)**: For time series forecasting.
- **Heroku**: Platform for deployment.