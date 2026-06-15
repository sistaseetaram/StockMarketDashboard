"""
Home Page - Market Trends and Financial News
"""

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Website URLs for web scraping
YAHOO_MOST_ACTIVE = "https://finance.yahoo.com/most-active"
YAHOO_GAINERS = "https://finance.yahoo.com/gainers"
YAHOO_LOSERS = "https://finance.yahoo.com/losers"
GOOGLE_NEWS_FINANCE = "https://news.google.com/search?pz=1&cf=all&hl=en-US&q=Finance&gl=US&ceid=US:en"

# Default headers to avoid blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


@st.cache_data(ttl=1800)
def parse_yahoo_finance(url: str) -> Optional[pd.DataFrame]:
    """
    Parse Yahoo Finance website for stock market data
    
    Args:
        url (str): Yahoo Finance URL
    
    Returns:
        Optional[pd.DataFrame]: DataFrame with top 5 stocks or None if error
    """
    try:
        page = requests.get(url, headers=HEADERS, timeout=10)
        page.raise_for_status()
        
        # Read HTML tables
        tables = pd.read_html(page.text)
        if not tables:
            st.warning("No data found from Yahoo Finance")
            return None
        
        stocks = tables[0].head(5)
        
        # Normalize column names
        stocks.columns = [col.replace(' ', '_').strip() for col in stocks.columns]
        
        # Drop commonly problematic columns if they exist
        cols_to_drop = [
            col for col in stocks.columns 
            if any(x in col for x in ['52_Wk', 'P/E', 'Ratio', 'Range'])
        ]
        stocks = stocks.drop(columns=cols_to_drop, errors='ignore')
        
        return stocks
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {url}: {str(e)}")
        st.error(f"Failed to fetch data: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Error parsing Yahoo Finance: {str(e)}")
        st.error(f"Error parsing data: {str(e)}")
        return None


@st.cache_data(ttl=1800)
def get_latest_news(url: str) -> Optional[pd.DataFrame]:
    """
    Scrape latest financial news from Google News
    
    Args:
        url (str): Google News URL
    
    Returns:
        Optional[pd.DataFrame]: DataFrame with top 5 news headlines or None
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract article headlines (Google News selector may change)
        articles = soup.find_all('article')
        headlines = set()
        
        for article in articles:
            try:
                headline = article.find('h3')
                if headline:
                    headlines.add(headline.get_text(strip=True))
            except Exception as e:
                logger.warning(f"Error extracting headline: {str(e)}")
                continue
        
        if not headlines:
            st.info("Unable to fetch current news headlines")
            return None
        
        df = pd.DataFrame(list(headlines)[:5], columns=['Headlines'])
        return df
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch news: {str(e)}")
        st.error(f"Failed to fetch news: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Error fetching news: {str(e)}")
        st.error(f"Error fetching news: {str(e)}")
        return None


def app():
    """Main home page app"""
    
    st.title('📊 Dashboard Home')
    
    st.markdown('''
    ---
    ### Welcome to the Stock Market Dashboard
    
    An interactive web application to visualize technical indicators, price information, 
    and forecasts for selected stock tickers.
    
    **Data Source**: [Yahoo! Finance](https://finance.yahoo.com/)
    ___
    ''')
    
    # Market Trends Section
    st.header("📈 Latest Market Trends")
    
    with st.expander("View Market Trends", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔥 Most Active", use_container_width=True):
                st.session_state.trend_selected = "most_active"
        
        with col2:
            if st.button("📈 Top Gainers", use_container_width=True):
                st.session_state.trend_selected = "gainers"
        
        with col3:
            if st.button("📉 Top Losers", use_container_width=True):
                st.session_state.trend_selected = "losers"
    
    # Display selected trend data
    if 'trend_selected' in st.session_state:
        selected_trend = st.session_state.trend_selected
        
        if selected_trend == "most_active":
            st.subheader("🔥 Most Active Stocks")
            with st.spinner("Loading most active stocks..."):
                data = parse_yahoo_finance(YAHOO_MOST_ACTIVE)
                if data is not None:
                    st.dataframe(data, use_container_width=True)
        
        elif selected_trend == "gainers":
            st.subheader("📈 Top Gainers")
            with st.spinner("Loading top gainers..."):
                data = parse_yahoo_finance(YAHOO_GAINERS)
                if data is not None:
                    st.dataframe(data, use_container_width=True)
        
        elif selected_trend == "losers":
            st.subheader("📉 Top Losers")
            with st.spinner("Loading top losers..."):
                data = parse_yahoo_finance(YAHOO_LOSERS)
                if data is not None:
                    st.dataframe(data, use_container_width=True)
    
    st.markdown("---")
    
    # Latest News Section
    st.header("📰 Latest Financial News")
    
    with st.spinner("Fetching latest news..."):
        news_df = get_latest_news(GOOGLE_NEWS_FINANCE)
        
        if news_df is not None:
            for idx, headline in enumerate(news_df['Headlines'], 1):
                st.write(f"{idx}. {headline}")
            
            st.markdown(
                "[📄 Read More Finance News](https://news.google.com/search?q=finance)",
                unsafe_allow_html=True
            )
        else:
            st.info("Unable to load news at this moment. Please try again later.")
    
    st.markdown("---")
    st.info(
        "💡 **Tip**: Use the sidebar to navigate to the Finance Dashboard for "
        "detailed technical analysis or the Prediction page for price forecasts."
    )
