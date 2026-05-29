# Project Objective and Summary

## Objective
The primary objective of this project is to create a comprehensive, real-time stock market dashboard web application.

## Project Summary
This repository contains the source code for a stock market dashboard built with Streamlit and designed to be deployed on Heroku. The project integrates financial data acquisition, exploratory data analysis (EDA), data visualization, and machine learning components to provide insights into stock market trends.

### Key Features and Workflow:
1. **Data Acquisition**: Fetches real-time financial data from sources like the Yahoo Finance API and Stocktwit API.
2. **Exploratory Data Analysis (EDA)**: Employs statistical methods such as moving averages, hypothesis testing, and confidence intervals to analyze market features.
3. **Data Visualization**: Utilizes various plots (box plots, histograms, density plots) to visualize daily and monthly stock price spreads, moving averages, volatility, and financial ratios (e.g., P/E ratio).
4. **Web Dashboard**: An interactive front-end built using Streamlit that consolidates all the data visualizations and insights into an accessible application.
5. **Machine Learning Pipeline**:
   - **Problem Formulation**: Identifying tasks suitable for predictive modeling.
   - **Data Preprocessing**: Handling data volatility, outliers, missing data, and imbalanced datasets, alongside data scaling.
   - **Model Selection & Feature Engineering**: Establishing benchmarks with simple linear models, identifying feature importance, and creating new features to optimize predictions.
   - **Hyperparameter Tuning & Validation**: Experimenting with different models and ensemble techniques (Bagging, Boosting, Stacking like Random Forest and GBDT) to finalize the best-performing model.
   - **Prediction & Performance Evaluation**: Running predictions on test and real-time data, checking model performance using appropriate metrics.
6. **Future Scalability**:
   - Developing sequence models (Deep Learning) for stock prediction.
   - Incorporating Natural Language Processing (NLP)/Natural Language Inference on current stock news by web scraping data and utilizing LSTMs or other state-of-the-art models for deeper market insights.
