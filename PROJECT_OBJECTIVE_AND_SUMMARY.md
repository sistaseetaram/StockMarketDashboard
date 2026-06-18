# Project Objective and Summary

## Objective
The main objective of this project is to create a real-time stock market dashboard.

## Key Features & Project Stages
1. **Data Acquisition**: Extract data using Yahoo Finance API and Stocktwit API.
2. **Exploratory Data Analysis (EDA)**: Understand features using statistical methods like moving averages, hypothesis testing, and confidence intervals.
3. **Data Visualization**: Visualize trends and volatility using box plots, histograms, and density plots for opening/closing prices, moving averages, and P/E ratios.
4. **Web Dashboard**: Create a base web application using Streamlit to showcase these insights, deployed on Heroku.
5. **Machine Learning Components**:
   - **Problem Formulation**: Identify ML tasks to predict or analyze stock data.
   - **Preprocessing**: Handle volatility, outliers, missing data, and imbalanced data, along with scaling.
   - **Model Selection & Feature Engineering**: Start with simple linear models as benchmarks. Iteratively add, evaluate, and select final features.
   - **Tuning & Validation**: Experiment with different models and ensemble techniques (like Random Forest, Gradient Boosting Decision Trees) and tune hyperparameters.
   - **Prediction & Performance**: Predict on test/real-time data and measure performance via suitable metrics.
6. **Prototype Deployment**: Deploy the fully functioning dashboard prototype.
7. **Scale Up**: Incorporate more complex deep learning techniques (like sequence models/LSTMs) and natural language inference from stock news for robust prediction.

## Application Architecture
The application is a multipage Streamlit web app deployed on Heroku. It includes:
- **Home**: Main landing view.
- **Finance Dashboard**: Real-time insights and visualizations of stock market data.
- **Prediction**: Machine learning models and predictions for real-time data.