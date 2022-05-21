import streamlit as st
from datetime import date

from dateutil.easter import easter
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

def app():
    st.title('Stock Forecast App')
    
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

    n_months = st.slider('Months of prediction:', 1, 4)
    period = n_months * 30
    
    data_load_state = st.text('Loading data...')
    data = load_data(ticker)
    data_load_state.text('Loading data... done!')

    plot_raw_data(data)
    
    # Predict forecast with Facebook Prophet
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Show and plot forecast 
    st.subheader('Forecast data')
    st.write(forecast.tail())
    
    st.write(f'Forecast plot for {n_months} months')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)