"""
Finance Dashboard - Technical Analysis Page
Displays candlestick charts, MACD, RSI, and volume indicators
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import logging

from apps.utils import get_ticker_selection, load_stock_data

logger = logging.getLogger(__name__)

# Default date range
START_DATE = "2015-01-01"


def calculate_macd(df: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    """
    Calculate MACD (Moving Average Convergence Divergence) indicators
    
    Args:
        df (pd.DataFrame): Stock data with 'Close' column
        fast (int): Fast EMA period (default 12)
        slow (int): Slow EMA period (default 26)
        signal (int): Signal line EMA period (default 9)
    
    Returns:
        pd.DataFrame: DataFrame with MACD, Signal, and Histogram columns
    """
    df['EMA_fast'] = df['Close'].ewm(span=fast, adjust=False).mean()
    df['EMA_slow'] = df['Close'].ewm(span=slow, adjust=False).mean()
    df['MACD'] = df['EMA_fast'] - df['EMA_slow']
    df['Signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    df['Histogram'] = df['MACD'] - df['Signal']
    df['Hist-Color'] = np.where(df['Histogram'] < 0, 'red', 'green')
    return df


def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Calculate RSI (Relative Strength Index)
    
    Args:
        df (pd.DataFrame): Stock data with 'Close' column
        period (int): RSI period (default 14)
    
    Returns:
        pd.DataFrame: DataFrame with RSI column
    """
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df


def plot_candlestick(df: pd.DataFrame, ticker: str) -> go.Figure:
    """
    Create candlestick chart with volume subplot
    
    Args:
        df (pd.DataFrame): Stock OHLCV data
        ticker (str): Stock ticker symbol
    
    Returns:
        go.Figure: Plotly figure object
    """
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_heights=[0.7, 0.2],
        subplot_titles=(f'{ticker} Price Chart', 'Volume')
    )
    
    # Candlestick trace
    fig.add_trace(
        go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='OHLC',
            increasing_line_color='green',
            decreasing_line_color='red'
        ),
        row=1, col=1
    )
    
    # Volume trace
    colors = ['red' if df['Close'].iloc[i] < df['Open'].iloc[i] else 'green' 
              for i in range(len(df))]
    fig.add_trace(
        go.Bar(
            x=df['Date'],
            y=df['Volume'],
            marker=dict(color=colors, line=dict(width=0)),
            name='Volume',
            showlegend=False
        ),
        row=2, col=1
    )
    
    fig.update_xaxes(rangeslider=dict(visible=False), row=1, col=1)
    fig.update_yaxes(title_text='Price ($)', row=1, col=1)
    fig.update_yaxes(title_text='Volume', row=2, col=1)
    
    fig.update_layout(
        height=600,
        title_text=f'{ticker} - Candlestick Chart with Volume',
        hovermode='x unified',
        xaxis_rangeslider_visible=False
    )
    
    return fig


def plot_macd_subplot(df: pd.DataFrame) -> go.Figure:
    """
    Create MACD subplot
    
    Args:
        df (pd.DataFrame): Stock data with MACD indicators
    
    Returns:
        go.Figure: Plotly figure object
    """
    fig = go.Figure()
    
    # Histogram
    fig.add_trace(go.Bar(
        x=df['Date'],
        y=df['Histogram'],
        marker_color=df['Hist-Color'],
        name='Histogram',
        showlegend=True
    ))
    
    # MACD line
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['MACD'],
        name='MACD',
        line=dict(color='darkorange', width=2.5)
    ))
    
    # Signal line
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Signal'],
        name='Signal',
        line=dict(color='cyan', width=2.5)
    ))
    
    fig.update_layout(
        title='MACD (Moving Average Convergence Divergence)',
        yaxis_title='MACD Value',
        xaxis_title='Date',
        height=400,
        hovermode='x unified'
    )
    
    return fig


def plot_rsi_subplot(df: pd.DataFrame) -> go.Figure:
    """
    Create RSI subplot
    
    Args:
        df (pd.DataFrame): Stock data with RSI
    
    Returns:
        go.Figure: Plotly figure object
    """
    fig = go.Figure()
    
    # RSI line
    fig.add_trace(go.Scatter(
        x=df['Date'].iloc[30:],
        y=df['RSI'].iloc[30:],
        name='RSI',
        line=dict(color='gold', width=2)
    ))
    
    # Overbought/Oversold zones
    fig.add_hline(y=70, line_dash='dash', line_color='red', 
                  annotation_text='Overbought (70)', annotation_position='right')
    fig.add_hline(y=30, line_dash='dash', line_color='green',
                  annotation_text='Oversold (30)', annotation_position='right')
    
    ymin = 25 if df['RSI'].iloc[30:].min() > 25 else df['RSI'].iloc[30:].min() - 5
    ymax = 75 if df['RSI'].iloc[30:].max() < 75 else df['RSI'].iloc[30:].max() + 5
    
    fig.update_layout(
        title='RSI (Relative Strength Index)',
        yaxis_title='RSI Value',
        xaxis_title='Date',
        height=400,
        yaxis_range=[ymin, ymax],
        hovermode='x unified'
    )
    
    return fig


def app():
    """Main finance dashboard app"""
    
    st.title('💼 Finance Dashboard')
    
    st.markdown('''
    ---
    ### Interactive Technical Analysis Dashboard
    View detailed price charts, volume data, and technical indicators for selected stocks.
    
    **Data Source**: [Yahoo! Finance](https://finance.yahoo.com/) (2015-Present)
    ___
    ''')
    
    # Get user inputs
    ticker = get_ticker_selection()
    
    # Date range selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "Start Date",
            value=datetime.strptime(START_DATE, "%Y-%m-%d"),
            help="Select historical data start date"
        )
    with col2:
        end_date = st.date_input(
            "End Date",
            value=datetime.now(),
            help="Select data end date"
        )
    
    # Load data
    with st.spinner(f'Loading {ticker} data...'):
        try:
            data = load_stock_data(
                ticker,
                start_date.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d")
            )
        except Exception as e:
            st.error(f"Failed to load data: {str(e)}")
            st.stop()
    
    # Display data summary
    st.subheader('📊 Data Summary')
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Current Price", f"${data['Close'].iloc[-1]:.2f}")
    with col2:
        st.metric("High (52w)", f"${data['High'].max():.2f}")
    with col3:
        st.metric("Low (52w)", f"${data['Low'].min():.2f}")
    with col4:
        st.metric("Avg Volume", f"{data['Volume'].mean():,.0f}")
    
    # Display raw data
    with st.expander("View Raw Data"):
        st.dataframe(data.head(10), use_container_width=True)
    
    st.markdown("---")
    
    # Calculate indicators
    data = calculate_macd(data)
    data = calculate_rsi(data)
    
    # Display charts
    st.subheader('📈 Price Chart')
    candlestick_fig = plot_candlestick(data, ticker)
    st.plotly_chart(candlestick_fig, use_container_width=True)
    
    st.subheader('🎯 MACD Indicator')
    macd_fig = plot_macd_subplot(data)
    st.plotly_chart(macd_fig, use_container_width=True)
    
    st.subheader('📊 RSI Indicator')
    rsi_fig = plot_rsi_subplot(data)
    st.plotly_chart(rsi_fig, use_container_width=True)
    
    st.markdown("---")
    st.info(
        "💡 **Technical Indicators Guide**:\n"
        "- **MACD**: Identifies momentum and trend direction\n"
        "- **RSI**: Measures overbought (>70) and oversold (<30) conditions"
    )
