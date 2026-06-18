# Project Summary: Stock Market Dashboard

## Objective
The primary objective of this project is to create a real-time stock market dashboard that provides insights through data visualization, exploratory data analysis (EDA), and machine learning predictions.

## Application Structure
The application is built as a multi-page web dashboard using **Streamlit** and is configured for deployment on Heroku. The main pages include:
- **Home:** Overview and initial data interactions.
- **Finance Dashboard:** Detailed financial metrics, visualizations, and EDA insights.
- **Prediction:** Machine learning-based forecasts on stock prices.

## Key Components & Workflow
1. **Data Acquisition:** Sourcing real-time financial data via Yahoo Finance API and Stocktwit API.
2. **Exploratory Data Analysis (EDA):** Utilizing statistical methods (moving averages, hypothesis testing, confidence intervals) to understand stock features.
3. **Data Visualization:** Creating box plots, histograms, and density plots to show price spread, volatility, and key financial ratios.
4. **Machine Learning Pipeline:**
   - **Preprocessing:** Handling volatility, outliers, missing data, and imbalanced data, along with data scaling.
   - **Model Selection & Feature Engineering:** Starting with linear benchmarks, adding features, and experimenting with ensembles (Random Forest, Gradient Boosting).
   - **Hyperparameter Tuning & Validation:** Tuning models and checking performance metrics on test/real-time data.
5. **Future Scaling (Planned):** Integrating Deep Learning (sequence models like LSTMs) and Natural Language Processing (NLP) to infer insights from web-scraped financial news.
