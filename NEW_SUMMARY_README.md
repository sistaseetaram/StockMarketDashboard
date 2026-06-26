# Project Summary: Real-Time Stock Market Dashboard

## Objective
The main objective of this project is to create a fully-functional, real-time stock market dashboard. The application is built using Streamlit to serve as a web interface, enabling users to explore and visualize financial data, and run machine learning models for predictions.

## Key Features & Task Overview

- **Data Acquisition**: Utilizing APIs like Yahoo Finance and Stocktwits to fetch real-time and historical financial data. Data scraping is also performed using libraries like `BeautifulSoup`.
- **Exploratory Data Analysis (EDA)**: Understanding market features using statistical methods like moving averages, hypothesis testing, and confidence intervals.
- **Data Visualization**: Extensive use of charting tools (e.g., Plotly) for generating box plots (daily/monthly spreads), histograms, density plots (moving averages, price-to-earnings), and other interactive financial charts.
- **Web Dashboard**: A multi-page Streamlit web application (`app.py`, integrating `home`, `financeDashboard`, and `prediction` modules) deployed on Heroku.
- **Machine Learning & Prediction**:
  - Framing predictive problems (e.g., forecasting stock prices) using linear models as benchmarks.
  - Feature engineering and hyperparameter tuning of ensemble models (Random Forest, GBDT).
  - Preprocessing techniques to handle volatility, missing data, imbalance, and scaling.
  - Future goals include Deep Learning sequence models (LSTM) and Natural Language Inference from scraped stock news.
- **Robust Architecture**: The project embraces multi-page architecture with centralized utilities, solid API request handling, caching capabilities, and comprehensive test coverage using `pytest`.

## Deployment
The repository is prepared for deployment on Heroku, complete with necessary configuration files such as `Procfile`, `setup.sh`, and `runtime.txt`.
