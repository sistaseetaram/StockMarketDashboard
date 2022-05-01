#%%
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup

#all the necessary website link
MostactiveLink="https://finance.yahoo.com/most-active"
gainerLink="https://finance.yahoo.com/gainers"
loserLink="https://finance.yahoo.com/losers"
cryptoLink="https://finance.yahoo.com/cryptocurrencies"
newslink="https://news.google.com/search?pz=1&cf=all&hl=en-IN&q=Finance&gl=IN&ceid=IN:en"


def app():

    #main page contents
    st.title('Dashboard Home')

    st.markdown('''
    ---
    #### An interactive web app to visualise technical indicators and price information for a ticker. 
    ##### Dataset retrieved from [Yahoo! Finance](https://uk.finance.yahoo.com/).
    ___
    ''')

    # parsing finance website
    def parse_Website(Link):
        page=requests.get(Link)
        soup=BeautifulSoup(page.text,'html.parser')
        Stocks=pd.read_html(page.text)[0]
        Stocks=Stocks.head(5)
        Stocks.columns = [c.replace(' ', '_') for c in Stocks.columns]
        if Link!=cryptoLink:
            Stocks=Stocks.drop(columns=['52_Week_Range','PE_Ratio_(TTM)'])
        else:
            try:
                Stocks=Stocks.drop(columns=['52_Week_Range','Day_Chart','Total_Volume_All_Currencies_(24Hr)','Volume_in_Currency_(24Hr)'])
            except:
                Stocks=Stocks.drop(columns=['52_Week_Range','Total_Volume_All_Currencies_(24Hr)','Volume_in_Currency_(24Hr)'])
        return Stocks

    #adds a horizontal line
    def addline():
        st.markdown('''
    ---
    ''')

    #method to parse Lates news
    def getNews(link):
        r=requests.get(link)
        html=r.content
        soup=BeautifulSoup(html,'html.parser')
        heading=soup.find_all('article',class_='MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne')
        titles=set()
        for t in heading:
            titles.add(t.h3.text)
        df=pd.DataFrame(titles)
        df=df.head(5)
        return df

    # top active, gainers and loosers tickers
    with st.expander("Check Latest Trends"):
        col1,col2,col3,col4=st.columns(4)
    with col1:
        mostActiveBtn=st.button("Most Active")
    with col2:
        gainersBtn=st.button("Gainers")
    with col3:
        losersBtn=st.button("Losers")
    with col4:
        cryptoBtn=st.button("Cryptocurrencies")
    

    #Presentation logic
    if mostActiveBtn:
        st.markdown("<h2 style='text-align: left;'>Most Active</h2>", unsafe_allow_html=True)
        mostActiveStock=parse_Website(MostactiveLink)
        st.dataframe(mostActiveStock)
    elif gainersBtn:
        st.markdown("<h2 style='text-align: left; color: Green;'>Top Gainer</h2>", unsafe_allow_html=True)
        gainersStock=parse_Website(gainerLink)
        st.dataframe(gainersStock)
    elif losersBtn:
        st.markdown("<h2 style='text-align: left; color: Red;'>Top Loser</h2>", unsafe_allow_html=True)
        loserStock=parse_Website(loserLink)
        st.dataframe(loserStock)
    elif cryptoBtn:
        st.markdown("<h2 style='text-align: left;'>Cryptocurrencies</h2>", unsafe_allow_html=True)
        crypto=parse_Website(cryptoLink)
        st.dataframe(crypto)

    addline()

    # displaying top 5 latest news
    with st.container():
        st.header('Latest News')
        newsDf=getNews(newslink)
        newsList=newsDf[0].to_list()
        for heading in newsList:
            st.text(heading)
        st.markdown('[More Finance News](https://news.google.com/search?pz=1&cf=all&hl=en-IN&q=Finance&gl=IN&ceid=IN:en)')
