# Project Summary: Stock Market Dashboard

## Objective
The primary objective of this project is to create a real-time stock market dashboard.

## Key Components

The project encompasses the following major phases and functionalities:

1. **Data Acquisition:** Fetching financial data from sources such as the Yahoo Finance API and Stocktwit API.
2. **Exploratory Data Analysis (EDA):** Utilizing statistical methods (moving averages, hypothesis testing, confidence intervals) to understand the features and data.
3. **Data Visualization:** Creating insightful visualizations including:
   - Box plots for daily and monthly stock price spread.
   - Histograms and density plots to show volatility and moving averages.
   - Density plots for various features like price-to-earning ratios.
4. **Web Dashboard:** A base web application built with Streamlit and designed for deployment on Heroku, showcasing all insights and visualizations.
5. **Machine Learning Pipeline:**
   - **Problem Formulation:** Defining specific tasks solvable via ML.
   - **Preprocessing:** Handling data volatility, outliers, missing data, imbalances, and scaling.
   - **Model Selection & Feature Engineering:** Establishing baselines with linear models, engineering new features based on importance, and selecting a final feature set.
   - **Tuning & Validation:** Experimenting with models, tuning hyperparameters, using ensemble techniques (e.g., Random Forests, GBDT), and finalizing the model.
   - **Prediction & Performance:** Evaluating the model on test/real-time data using appropriate metrics.
6. **Deployment & Scaling:** Deploying the prototype and scaling the project by potentially adding sequence models (Deep Learning) or performing natural language inference on stock news using web scraping and LSTMs.
