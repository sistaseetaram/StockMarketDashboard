# Stock Market Dashboard Project Summary

## Objective
The primary objective of this project is to create a real-time stock market dashboard.

## Technical Stack
*   **Web Framework:** Streamlit (Multi-page application)
*   **Data Acquisition:** Yahoo Finance API, Stocktwits API
*   **Deployment:** Heroku

## Task List & Features
*   **Data Acquisition:** Gather data from Yahoo Finance and Stocktwits.
*   **Exploratory Data Analysis (EDA):** Analyze features and data using statistical methods (moving averages, hypothesis testing, confidence intervals).
*   **Data Visualization:**
    *   Box plots for opening/closing prices to show daily and monthly spread.
    *   Histograms and density plots for moving average and volatility.
    *   Density plots for features like price-to-earnings ratio.
*   **Web Dashboard:** Develop a base web application using Streamlit to display insights and deploy it on Heroku.
*   **Machine Learning Problem Formulation:** Identify tasks solvable using ML.
*   **Preprocessing:**
    *   Handle data volatility, outliers, and missing data.
    *   Address data imbalance.
    *   Scale data.
*   **Model Selection and Feature Engineering:**
    *   Set benchmarks with simple linear models.
    *   Evaluate feature importance and iteratively add features.
    *   Finalize the feature set.
*   **Hyperparameter Tuning, Validation, and Finalization:**
    *   Experiment with different models and tune hyperparameters.
    *   Test ensemble methods like Bagging, Boosting, and Stacking (e.g., Random Forest, GBDT).
    *   Finalize the predictive model.
*   **Prediction and Performance Evaluation:**
    *   Make predictions on test and real-time data.
    *   Evaluate performance using appropriate metrics.
*   **Prototype Deployment:** Deploy the fully functional prototype.
*   **Scaling Up:**
    *   Develop a sequence model (Deep Learning) for the same task.
    *   Implement Natural Language Inference from current stock news using web scraping, LSTMs, and other advanced techniques.

## Application Architecture
The application uses a multi-page structure:
*   **Home (`apps/home.py`):** General overview and stock scraping logic.
*   **Finance Dashboard (`apps/financeDashboard.py`):** Detailed financial analysis and metrics (e.g., RSI, MACD).
*   **Prediction (`apps/prediction.py`):** Machine learning model predictions.
*   **Main Entry Point (`app.py`):** Combines the individual pages using the `multiapp.py` framework.
