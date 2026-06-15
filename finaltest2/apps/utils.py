"""
Utility functions for the Stock Market Dashboard
"""

import streamlit as st
import pandas as pd
import yfinance as yf
from typing import Dict
from datetime import datetime, timedelta

# Stock ticker configuration
STOCK_TICKER_MAP: Dict[str, str] = {
    'GOOGLE (GOOG)': 'GOOG',
    'S&P 500 (^GSPC)': '^GSPC',
    'Microsoft Corporation (MSFT)': 'MSFT',
    'NIFTY 50 (^NSEI)': '^NSEI',
    'Apple Inc. (AAPL)': 'AAPL',
    'Amazon.com (AMZN)': 'AMZN',
    'Tesla Inc. (TSLA)': 'TSLA',
}

def get_ticker_selection() -> str:
    """
    Display stock ticker selection widget
    
    Returns:
        str: The selected stock ticker symbol
    """
    stocks = tuple(STOCK_TICKER_MAP.keys())
    selected_stock = st.selectbox(
        'Select dataset for analysis',
        stocks,
        help="Choose a stock ticker to analyze"
    )
    return STOCK_TICKER_MAP[selected_stock]


@st.cache_data(ttl=3600)
def load_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download historical stock data from Yahoo Finance
    
    Args:
        ticker (str): Stock ticker symbol
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
    
    Returns:
        pd.DataFrame: Historical OHLCV data
    
    Raises:
        Exception: If data download fails
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}")
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        st.error(f"Error loading data for {ticker}: {str(e)}")
        raise


def calculate_moving_averages(df: pd.DataFrame, periods: list = [20, 50, 200]) -> pd.DataFrame:
    """
    Calculate Exponential Moving Averages (EMA)
    
    Args:
        df (pd.DataFrame): Stock data with 'Close' column
        periods (list): List of periods for EMAs
    
    Returns:
        pd.DataFrame: DataFrame with EMA columns added
    """
    for period in periods:
        df[f'EMA_{period}'] = df['Close'].ewm(span=period, adjust=False).mean()
    return df


def validate_date_range(start_date: str, end_date: str, min_days: int = 30) -> bool:
    """
    Validate that the date range is appropriate for analysis
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        min_days (int): Minimum required days of data
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return (end - start).days >= min_days
    except ValueError:
        return False
