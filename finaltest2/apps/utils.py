import streamlit as st

STOCK_TICKER_MAP = {
    'GOOGLE(GOOG)': 'GOOG',
    'S&P 500 (^GSPC)': '^GSPC',
    'Microsoft Corporation (MSFT)': 'MSFT',
    'NIFTY 50 (^NSEI)': '^NSEI'
}

def get_ticker_selection():
    stocks = tuple(STOCK_TICKER_MAP.keys())
    selectedStock = st.selectbox('Select dataset for prediction', stocks)
    return STOCK_TICKER_MAP[selectedStock]
