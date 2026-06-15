"""
Prediction Page - Stock Price Forecasting using Prophet
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import logging

try:
    from prophet import Prophet
    from prophet.plot import plot_plotly
except ImportError:
    from fbprophet import Prophet
    from fbprophet.plot import plot_plotly

import plotly.graph_objects as go
from apps.utils import get_ticker_selection, load_stock_data

logger = logging.getLogger(__name__)

START_DATE = "2015-01-01"


@st.cache_data(ttl=3600)
def load_data_for_prophet(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Load historical data for Prophet model"""
    data = load_stock_data(ticker, start_date, end_date)
    return data[['Date', 'Close']].copy()


def plot_raw_data(data: pd.DataFrame, ticker: str) -> None:
    """Plot raw stock data with open and close prices"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Open'],
        name='Open Price',
        line=dict(color='blue')
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        name='Close Price',
        line=dict(color='orange')
    ))
    
    fig.update_layout(
        title=f'{ticker} - Historical Price Data',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        height=500,
        hovermode='x unified',
        xaxis_rangeslider_visible=True
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_prophet_forecast(data: pd.DataFrame, periods: int, yearly_seasonality: bool = True, weekly_seasonality: bool = True) -> tuple:
    """Create Prophet model and generate forecast"""
    try:
        df_train = data.rename(columns={'Date': 'ds', 'Close': 'y'})
        
        model = Prophet(
            yearly_seasonality=yearly_seasonality,
            weekly_seasonality=weekly_seasonality,
            daily_seasonality=False,
            interval_width=0.95,
            changepoint_prior_scale=0.05
        )
        
        with st.spinner('Training Prophet model...'):
            model.fit(df_train)
        
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        
        return model, forecast
    
    except Exception as e:
        logger.error(f"Error creating Prophet forecast: {str(e)}")
        raise


def app():
    """Main prediction app"""
    
    st.title('🔮 Stock Price Forecast')
    
    st.markdown('''
    ---
    ### AI-Powered Price Prediction
    Forecast future stock prices using Facebook's Prophet time-series forecasting model.
    
    **Note**: Forecasts are based on historical patterns and should not be considered investment advice.
    ___
    ''')
    
    ticker = get_ticker_selection()
    
    col1, col2 = st.columns(2)
    with col1:
        n_months = st.slider('Forecast Period (Months)', min_value=1, max_value=12, value=3, help="Number of months to forecast ahead")
    with col2:
        period_days = n_months * 30
    
    with st.spinner(f'Loading historical data for {ticker}...'):
        try:
            today = datetime.now()
            end_date = today.strftime("%Y-%m-%d")
            data = load_data_for_prophet(ticker, START_DATE, end_date)
            
            if len(data) < 100:
                st.warning(f"⚠️ Only {len(data)} days of data available. Prophet works best with at least 100 data points.")
        except Exception as e:
            st.error(f"Failed to load data: {str(e)}")
            st.stop()
    
    st.subheader('📊 Historical Price Data')
    plot_raw_data(data, ticker)
    
    with st.expander("Model Configuration"):
        col1, col2 = st.columns(2)
        with col1:
            yearly_seasonality = st.checkbox('Enable Yearly Seasonality', value=True, help="Account for yearly patterns in stock price")
        with col2:
            weekly_seasonality = st.checkbox('Enable Weekly Seasonality', value=True, help="Account for weekly patterns in stock price")
    
    if st.button('Generate Forecast', use_container_width=True):
        try:
            model, forecast = create_prophet_forecast(data, period_days, yearly_seasonality=yearly_seasonality, weekly_seasonality=weekly_seasonality)
            
            st.success('✅ Forecast generated successfully!')
            
            st.subheader('📈 Forecast Results')
            forecast_display = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
            forecast_display.columns = ['Date', 'Forecast', 'Lower Bound', 'Upper Bound']
            forecast_display = forecast_display[forecast_display['Date'] > data['Date'].max()]
            
            st.dataframe(forecast_display.tail(20), use_container_width=True, hide_index=True)
            
            st.subheader('🎯 Forecast Visualization')
            fig = plot_plotly(model, forecast)
            fig.update_layout(title=f'{ticker} - {n_months} Month Price Forecast', xaxis_title='Date', yaxis_title='Price (USD)', height=600, hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('📊 Forecast Summary')
            col1, col2, col3, col4 = st.columns(4)
            
            last_price = data['Close'].iloc[-1]
            forecast_price = forecast['yhat'].iloc[-1]
            lower_bound = forecast['yhat_lower'].iloc[-1]
            upper_bound = forecast['yhat_upper'].iloc[-1]
            price_change = forecast_price - last_price
            percent_change = (price_change / last_price) * 100
            
            with col1:
                st.metric("Current Price", f"${last_price:.2f}")
            with col2:
                st.metric("Forecasted Price", f"${forecast_price:.2f}", f"{percent_change:+.2f}%")
            with col3:
                st.metric("Lower Bound (95%)", f"${lower_bound:.2f}")
            with col4:
                st.metric("Upper Bound (95%)", f"${upper_bound:.2f}")
            
            if yearly_seasonality or weekly_seasonality:
                st.subheader('🔍 Forecast Components')
                fig_components = model.plot_components(forecast)
                st.pyplot(fig_components)
        
        except Exception as e:
            logger.error(f"Error generating forecast: {str(e)}")
            st.error(f"❌ Error generating forecast: {str(e)}")
    
    st.markdown("---")
    st.warning("⚠️ **Disclaimer**: This forecast is based on historical patterns and machine learning algorithms. It should not be used as investment advice. Always conduct your own research and consult with financial advisors.")
