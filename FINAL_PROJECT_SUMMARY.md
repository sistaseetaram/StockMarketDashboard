# Final Project Summary

## Objective
The primary objective of this project is to create a real-time stock market dashboard.

## Application Architecture
The dashboard is built as a multi-page web application using **Streamlit**. The main entry point is `finaltest2/app.py`, which loads individual application pages located in the `finaltest2/apps/` directory, such as the Home, Finance Dashboard, and Prediction pages. The app is configured for deployment on Heroku.

## Task Checklist
The project entails a comprehensive lifecycle divided into several core components:

1. **Data Acquisition:**
   Fetching financial and market data from sources such as the Yahoo Finance API and Stocktwit API.

2. **Exploratory Data Analysis (EDA):**
   Understanding features using statistical methods like moving averages, hypothesis testing, and confidence intervals.

3. **Data Visualization:**
   Plotting stock price spreads (box plots), moving average/volatility (histograms/density plots), and financial metrics (e.g., price-to-earning ratios).

4. **Web Dashboard Integration:**
   Building a functional, interactive user interface with Streamlit to display insights.

5. **Machine Learning Formulation:**
   Defining predictive tasks that can be addressed using Machine Learning.

6. **Preprocessing:**
   Handling data volatility, outliers, missing values, class imbalance, and scaling.

7. **Model Selection & Feature Engineering:**
   Establishing benchmarks with simple linear models, followed by iterative feature engineering to select the final feature set.

8. **Hyperparameter Tuning & Validation:**
   Experimenting with ensembles (Bagging, Boosting, Stacking like Random Forests and GBDTs), tuning parameters, and finalizing the model.

9. **Prediction & Performance Checks:**
   Applying the model to test and real-time data to evaluate its performance against appropriate metrics.

10. **Prototype Deployment:**
    Deploying the fully functioning machine learning prototype into the dashboard.

11. **Future Scaling:**
    Scaling up by introducing Deep Learning (sequence models) and NLP techniques (analyzing web-scraped financial news using LSTMs).
