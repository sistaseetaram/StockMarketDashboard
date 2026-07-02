# Project Summary: Stock Market Dashboard

## Objective
The primary objective of this project is to build and deploy a **real-time stock market dashboard**. This dashboard aims to provide insights into stock market data through exploratory data analysis (EDA), data visualization, and predictive machine learning models, all accessible via a unified web interface.

## Architecture & Frameworks
- **Framework**: Streamlit (Multi-page application architecture)
- **Deployment**: Configured for deployment on Heroku.
- **Data Sources**: Yahoo Finance API, Stocktwit API, and web scraping for current stock news.

## Application Pages
The application is structured into multiple pages for a seamless user experience:
1. **Home**: Overview and initial insights.
2. **Finance Dashboard**: Detailed exploratory data analysis (EDA) and visualizations.
3. **Prediction**: Machine learning-based stock predictions and performance evaluation.

## Key Features & Task Breakdown
- **Data Acquisition**: Fetching real-time and historical financial data from external APIs.
- **Exploratory Data Analysis (EDA)**: Understanding data through statistical methods like moving averages, hypothesis testing, and confidence intervals.
- **Data Visualization**: Displaying data distributions and trends using box plots, histograms, and density plots for daily/monthly stock prices and volatility.
- **Machine Learning**:
  - Formulating stock prediction problems.
  - **Preprocessing**: Handling volatility, outliers, missing data, and scaling.
  - **Model Selection & Feature Engineering**: Establishing benchmarks using linear models, evaluating feature importance, and finalizing feature sets.
  - **Hyperparameter Tuning & Ensembling**: Using techniques like Random Forest (RF) and Gradient Boosting Decision Trees (GBDT).
  - **Prediction & Evaluation**: Running predictions on test data and real-time streams to validate performance.
- **Future Scaling**:
  - Deep Learning (Sequence Models) for enhanced prediction tasks.
  - Natural Language Inference (NLP) utilizing LSTMs on scraped financial news.
