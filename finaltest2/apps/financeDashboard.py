#importing all the necessary libraries
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

#required functions

#calcualtes the value of MACD along with Signal and Histogram and adds it to Dataframe before returning it.
def getMACD(df, column='Adj Close'):
    df['EMA12'] = df[column].ewm(span=12, adjust=False).mean() #calculating EMA12
    df['EMA26'] = df[column].ewm(span=26, adjust=False).mean() #calculating EMA26
    df['MACD'] = df['EMA12'] - df['EMA26']  # MACD=EMA12-EMA26
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()  # Signal= 9day EMA of MACD.
    df['Histogram'] = df['MACD'] - df['Signal']  # Histogram = MACD - Indicator.
    return df

#calcualtes the value of RSI and adds it to Dataframe before returning it.
def getRSI(df, column='Adj Close', time=14):
    difference=df[column].diff(1) #preservers dimensions off diff values.
    upChange=0*difference
    downChange=0*difference
    upChange[difference > 0] = difference[difference > 0] # Up change is positive difference, otherwise it is zero.
    downChange[difference < 0] = difference[difference < 0] # Down change is Negative difference, otherwise it is zero.
    upChangeAvg= upChange.ewm(com=time - 1,min_periods=time).mean()
    downChangeAvg = downChange.ewm(com=time - 1,min_periods=time).mean()
    RS = abs(upChangeAvg/downChangeAvg)
    df['RSI'] = 100 - 100 / (1 + RS)
    return df


#return graph object for candlestick charts
def plot_candlestick_chart(fig, df, row, column=1, plot_EMAs=True, plot_strategy=True):
    fig.add_trace(go.Candlestick(x=df['Date'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='Candlestick Chart'),row=row,col=column)
    if (plot_EMAs == True):
        fig.add_trace(go.Scatter(x=df['Date'],
                                 y=df['EMA12'],
                                 name='12-period EMA',
                                 line=dict(color='dodgerblue', width=2)),
                      row=row,
                      col=column)
        fig.add_trace(go.Scatter(x=df['Date'],
                                 y=df['EMA26'],
                                 name='26-period EMA',
                                 line=dict(color='whitesmoke', width=2)),
                      row=row,
                      col=column)    
    fig.update_xaxes(rangeslider={'visible': False})
    fig.update_yaxes(title_text='Price ($)', row=row, col=column)
    return fig

#return graph object with histogram, MACD, Signal
def plot_MACD(fig, df, row, column=1):
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

#return graph object containing RSI
def plot_RSI(fig, df, row, column=1):
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

#return graph object containing Volume
def plot_volume(fig, df, row, column=1):
    fig.add_trace(go.Bar(x=df['Date'],
                         y=df['Volume'],
                         marker=dict(color='lightskyblue',line=dict(color='firebrick', width=0.1)),
                         showlegend=False,
                         name='Volume'),
                  row=row,
                  col=column)
    fig.update_xaxes(title_text='Date', row=4, col=1)
    fig.update_yaxes(title_text='Volume ($)', row=row, col=column)
    return fig

#main content 
def app():
    st.title('Finance Dashboard')

    #text to appear on page
    st.markdown('''
    ---
    #### An interactive visualization and analysis web page for selected Companies ticker.
    ##### Dataset retrieved from [Yahoo! Finance](https://uk.finance.yahoo.com/) (2015-2022).
    ''')

    #logic to pick and store the selected ticker of a stock for later use
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

    #message to be displayed
    data_load_state = st.text('Loading data...')
    data = load_data(ticker)
    data_load_state.text('Loading data... done!')
    x1,x2=st.columns(2)

    st.text('Sample Dataset')
    df=data.head(5)
    st.dataframe(df)

    st.markdown("<br><br>",unsafe_allow_html=True)

    data = getMACD(data)
    data = getRSI(data)
    fig = make_subplots(rows=4,cols=1,shared_xaxes=True,vertical_spacing=0.006,row_width=[0.2, 0.3, 0.3, 0.8])
    fig = plot_candlestick_chart(fig,data,row=1,plot_EMAs=True,plot_strategy=True)
    fig = plot_MACD(fig, data, row=2)
    fig = plot_volume(fig, data, row=4)
    fig = plot_RSI(fig, data, row=3)

    #choosing the presentation and layout for evry figure
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

    #plotting the figures
    st.plotly_chart(fig)  