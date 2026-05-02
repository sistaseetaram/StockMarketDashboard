# Real-Time Stock Market Dashboard

## Objective
The primary objective of this project is to build a real-time stock market dashboard. It provides an interactive web application designed to visualize technical indicators, historical price data, and stock forecasts. The project serves as an end-to-end data science and machine learning application, covering data acquisition, exploratory data analysis (EDA), visualization, machine learning formulation, prediction, and deployment.

## Summary
The application is built using a multi-page architecture with the **Streamlit** framework.

### Architecture and Tech Stack
- **Frontend & Routing**: Managed via `app.py` and a custom multi-page framework (`multiapp.py`). Pages include Home, Finance Dashboard, and Prediction, located in the `apps/` directory.
- **Data Acquisition**: Utilizes the `yfinance` API for real-time and historical stock data.
- **Web Scraping**: Extracts top market movers (gainers, losers, active) and financial news from Yahoo Finance and Google News using `BeautifulSoup`.
- **Data Visualization**: Leverages `Plotly` (specifically `graph_objects` and `subplots`) for responsive candlestick charts, volume bars, and technical indicators.
- **Forecasting / Machine Learning**: Utilizes Facebook's `Prophet` library for time-series stock price forecasting.
- **Deployment Ready**: Configured for cloud deployment (e.g., Heroku), utilizing files like `Procfile`, `setup.sh`, and `runtime.txt`.

### Key Features
- **Real-Time Market Data**: Live scraping of active trends and recent financial news.
- **Technical Analysis Dashboard**: Automatic calculation and interactive plotting of key indicators like MACD (Moving Average Convergence Divergence) and RSI (Relative Strength Index).
- **Time-Series Forecasting**: Users can predict future stock prices for a specified horizon (1 to 4 months) and visualize the forecast alongside raw data using Facebook's Prophet.
- **Scalable Multipage UI**: Easy navigation between different analytical views and models, including Home, Finance Dashboard, and Prediction.

### Future Roadmap
- Scale up the project by adding functionalities like deep learning sequence models (LSTM) to achieve the same task and check performance.
- Perform Natural Language Inference from current stock news by web scraping the news data and applying state-of-the-art NLP techniques to assess market sentiment.
- Improve handling of data volatility, outliers, missing data, and class imbalance.
- Implement ensembles like Random Forests (RF), Gradient Boosting Decision Trees (GBDT), and stacking techniques.
