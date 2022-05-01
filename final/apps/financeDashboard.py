import streamlit as st
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from datetime import date
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#setting data range for our dataset
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#load dataset
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

#functions

def get_MACD(df, column='Adj Close'):
    """Return a DataFrame with the MACD indicator and related information (signal line and histogram)."""
    df['EMA-12'] = df[column].ewm(span=12, adjust=False).mean()
    df['EMA-26'] = df[column].ewm(span=26, adjust=False).mean()
    # MACD will be equak to 12-Period EMA − 26-Period EMA.
    df['MACD'] = df['EMA-12'] - df['EMA-26']
    # Signal line will be 9-day EMA of the MACD line.
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    # Histogram = MACD - Indicator.
    df['Histogram'] = df['MACD'] - df['Signal']
    return df


def get_RSI(df, column='Adj Close', time_window=14):
    """Return a DataFrame with the RSI indicator for the specified time window."""
    diff = df[column].diff(1)
    # This preservers dimensions off diff values.
    up_chg = 0 * diff
    down_chg = 0 * diff
    # Up change is equal to the positive difference, otherwise equal to zero.
    up_chg[diff > 0] = diff[diff > 0]
    # Down change is equal to negative deifference, otherwise equal to zero.
    down_chg[diff < 0] = diff[diff < 0]
    # We set com = time_window-1 so we get decay alpha=1/time_window.
    up_chg_avg = up_chg.ewm(com=time_window - 1,
                            min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1,
                                min_periods=time_window).mean()
    RS = abs(up_chg_avg / down_chg_avg)
    df['RSI'] = 100 - 100 / (1 + RS)
    return df


def get_trading_strategy(df, column='Adj Close'):
    """Return the Buy/Sell signal on the specified (price) column (Default = 'Adj Close')."""
    buy_list, sell_list = [], []
    flag = False
    for i in range(0, len(df)):
        if df['MACD'].iloc[i] > df['Signal'].iloc[i] and flag == False:
            buy_list.append(df[column].iloc[i])
            sell_list.append(np.nan)
            flag = True
        elif df['MACD'].iloc[i] < df['Signal'].iloc[i] and flag == True:
            buy_list.append(np.nan)
            sell_list.append(df[column].iloc[i])
            flag = False
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
    # Store the buy and sell signals/lists into the DataFrame.
    df['Buy'] = buy_list
    df['Sell'] = sell_list
    return df


def plot_candlestick_chart(fig, df, row, column=1, plot_EMAs=True, plot_strategy=True):
    """Return a graph object figure containing a Candlestick chart in the specified row."""
    fig.add_trace(go.Candlestick(x=df['Date'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='Candlestick Chart'),row=row,col=column)
    if (plot_EMAs == True):
        fig.add_trace(go.Scatter(x=df['Date'],
                                 y=df['EMA-12'],
                                 name='12-period EMA',
                                 line=dict(color='dodgerblue', width=2)),
                      row=row,
                      col=column)
        fig.add_trace(go.Scatter(x=df['Date'],
                                 y=df['EMA-26'],
                                 name='26-period EMA',
                                 line=dict(color='whitesmoke', width=2)),
                      row=row,
                      col=column)    
    fig.update_xaxes(rangeslider={'visible': False})
    fig.update_yaxes(title_text='Price ($)', row=row, col=column)
    return fig


def plot_MACD(fig, df, row, column=1):
    """Return a graph object figure containing the MACD indicator, the signal line, and a histogram in the specified row."""
    df['Hist-Color'] = np.where(df['Histogram'] < 0, 'red', 'green')

    fig.add_trace(go.Bar(x=df['Date'],
                         y=df['Histogram'],
                         name='Histogram',
                         marker_color=df['Hist-Color'],
                         showlegend=True),
                  row=row,
                  col=column)

    fig.add_trace(go.Scatter(x=df['Date'],
                             y=df['MACD'],
                             name='MACD',
                             line=dict(color='darkorange', width=2.5)),
                  row=row,
                  col=column)

    fig.add_trace(go.Scatter(x=df['Date'],
                             y=df['Signal'],
                             name='Signal',
                             line=dict(color='cyan', width=2.5)),
                  row=row,
                  col=column)

    fig.update_yaxes(title_text='MACD', row=row, col=column)

    return fig


def plot_RSI(fig, df, row, column=1):
    """Return a graph object figure containing the RSI indicator in the specified row."""
    fig.add_trace(go.Scatter(x=df['Date'].iloc[30:],
                             y=df['RSI'].iloc[30:],
                             name='RSI',
                             line=dict(color='gold', width=2)),
                  row=row,
                  col=column)
    fig.update_yaxes(title_text='RSI', row=row, col=column)
    ymin = 25 if df['RSI'].iloc[30:].min() > 25 else df['RSI'].iloc[30:].min() - 5
    ymax = 75 if df['RSI'].iloc[30:].max() < 75 else df['RSI'].iloc[30:].max() + 5
    fig.update_yaxes(range=[ymin, ymax], row=row, col=column)
    return fig


def plot_volume(fig, df, row, column=1):
    """Return a graph object figure containing the volume chart in the specified row."""
    fig.add_trace(go.Bar(x=df['Date'],
                         y=df['Volume'],
                         marker=dict(color='lightskyblue',
                                     line=dict(color='firebrick', width=0.1)),
                         showlegend=False,
                         name='Volume'),
                  row=row,
                  col=column)

    fig.update_xaxes(title_text='Date', row=4, col=1)
    fig.update_yaxes(title_text='Volume ($)', row=row, col=column)

    return fig


def app():
    st.title('Finance Dashboard')

    st.markdown('''
    ---
    #### An interactive visualization and analysis web page for selected Companies ticker.
    ##### Dataset retrieved from [Yahoo! Finance](https://uk.finance.yahoo.com/) (2015-2022).
    ''')

    ticker=''
    stocks=('GOOGLE(GOOG)', 'S&P 500 (^GSPC)', 'Microsoft Corporation (MSFT)', 'NIFTY 50 (^NSEI)')
    selectedStock = st.selectbox('Select dataset for prediction', stocks)

    if selectedStock=='GOOGLE(GOOG)':
        ticker='GOOG'
    elif selectedStock=='S&P 500 (^GSPC)':
        ticker='^GSPC'
    elif selectedStock=='Microsoft Corporation (MSFT)':
        ticker='MSFT'
    elif selectedStock=='NIFTY 50 (^NSEI)':
        ticker='^NSEI'

    
    data_load_state = st.text('Loading data...')
    data = load_data(ticker)
    data_load_state.text('Loading data... done!')
    x1,x2=st.columns(2)

    st.text('Sample Dataset')
    df=data.head(5)
    st.dataframe(df)

    st.markdown("<br><br>",unsafe_allow_html=True)

    data = get_MACD(data)
    data = get_RSI(data)
    data=df = get_trading_strategy(data)

    fig = make_subplots(rows=4,cols=1,shared_xaxes=True,vertical_spacing=0.006,row_width=[0.2, 0.3, 0.3, 0.8])
    fig = plot_candlestick_chart(fig,data,row=1,plot_EMAs=True,plot_strategy=True)
    fig = plot_MACD(fig, data, row=2)
    fig = plot_volume(fig, data, row=4)
    fig = plot_RSI(fig, data, row=3)

    fig.update_layout(width=1100, height=800,plot_bgcolor='#0E1117',paper_bgcolor='#0E1117',
                    title={'text': '{} - Dashboard'.format(ticker),'y': 0.98},
                    hovermode='x unified',
                    legend=dict(orientation='h',
                    xanchor='left',x=0.05,yanchor='bottom',y=1.003))
    
    axis_lw, axis_color = 2, 'white'

    fig.update_layout(xaxis1=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                        yaxis1=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                        font=dict(color=axis_color))

    fig.update_layout(xaxis2=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    yaxis2=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    font=dict(color=axis_color))

    fig.update_layout(xaxis3=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    yaxis3=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    font=dict(color=axis_color))

    fig.update_layout(xaxis4=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    yaxis4=dict(linewidth=axis_lw,linecolor=axis_color,mirror=True,showgrid=False),
                    font=dict(color=axis_color))

    st.plotly_chart(fig)