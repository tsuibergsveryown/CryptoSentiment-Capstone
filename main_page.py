import streamlit as st
import time
import numpy as np
import pandas as pd
import altair as lt
import seaborn as sns
import matplotlib.pyplot as plt
#import price_pred
#import recommendation


# Sidebar Selection

#PAGES = {
#    'Main Page': main_page,
#    'Price Prediction with Sentimental Analysis': price_pred,
#    'Recommendation': recommendation,
#}

st.sidebar.title('CryptoSentiment')
#selection = st.sidebar.radio("To page", list(PAGES.keys()))
#page = PAGES[selection]
#page.app()



def app():
    st.write("""
    # Bitcoin Price Prediction with Sentimental Analysis

    For this capstone project, I've compiled data of the top 3 cryptocurrencies by market cap to from as early as 2013 to 2021, as well as public's sentiments via social networks such as readdit and google trend.

    I then compare the price with public sentiment of a given cryptocurrency (bitcoin in this case) to predict its price.

    Here, I'm showing the correlation between top 3 cryptocurrecies and 1 meme cryptocurrency (Dogecoin), with the google trend and readdit sentiment.

    The top 3 cryptocurrencies by market cap currently is:

    **1. Bitcoin (BTC)**, _$928B_

    **2. Ethereum (ETH)**, _$381B_

    **3. Cardano (ADA)**, _$87B_

    and the meme coin that took everyone by surprised is:

    **1. Dogecoin (DOG)**, _$42B (ranked #7)_

    """)

    st.write(""" 
    
    
    
    
    """)

    # Load Data
    df_btc = pd.read_csv('cryptodata/cleaned_btc.csv')
    df_eth = pd.read_csv('cryptodata/cleaned_eth.csv')
    df_ada = pd.read_csv('cryptodata/cleaned_ada.csv')
    df_dog = pd.read_csv('cryptodata/cleaned_dog.csv')
    df_close3 = pd.read_csv('cryptodata/3coinsclose.csv')
    google_trend_5y = pd.read_csv('data/google_trend_5y.csv')
    google_trend_3m = pd.read_csv('data/google_trend_3m.csv')
    readdit_3m = pd.read_csv('data/df_3m_price_polarity.csv')
    btc_price_polarity_trend = pd.read_csv('data/btc_price_polarity_trend.csv')

    with st.expander("See BTC Price from 2013-2021"):
        fig = plt.figure(figsize=(12, 9))
        plt.plot(df_btc['Date'], df_btc['Close'], label='Closing Price') #blue line
        plt.plot(df_btc['Close'].rolling(30).mean(), label='30 Days Moving Average')  #orange line
        plt.plot(df_btc['Close'].diff(), label='') #green line
        plt.plot(df_btc['Close'].pct_change(), label='Percentage Change Daily') #red line
        plt.legend()
        steps=550
        plt.xticks(df_btc.index[0::steps], fontsize=10)
        st.write(fig)

    with st.expander("ETH Price from 2013 - 2021"):
        fig = plt.figure(figsize=(12, 9))
        plt.plot(df_eth['Date'], df_eth['Close'], label='Closing Price')
        plt.plot(df_eth['Close'].rolling(30).mean(), label = '30 Days Moving Average')
        plt.plot(df_eth['Close'].diff(), label='Difference of the day')
        plt.plot(df_eth['Close'].pct_change(), label='Percentage Change Daily')
        plt.legend()
        steps=550
        plt.xticks(df_eth.index[0::steps], fontsize=10)
        st.write(fig)

    with st.expander("ADA Price from 2013 - 2021"):
        fig = plt.figure(figsize=(12, 9))
        plt.plot(df_ada['Date'], df_ada['Close'], label='Closing Price')
        plt.plot(df_ada['Close'].rolling(30).mean(), label = '30 Days Moving Average')
        plt.plot(df_ada['Close'].diff(), label='Difference of the day')
        plt.plot(df_ada['Close'].pct_change(), label='Percentage Change Daily')
        plt.legend()
        steps=550
        plt.xticks(df_ada.index[0::steps], fontsize=10)
        st.write(fig)

    with st.expander("DOG Price from 2013 - 2021"):
        fig = plt.figure(figsize=(12, 9))
        plt.plot(df_dog['Date'], df_dog['Close'], label='Closing Price')
        plt.plot(df_dog['Close'].rolling(30).mean(), label = '30 Days Moving Average')
        plt.plot(df_dog['Close'].diff(), label='Difference of the day')
        plt.plot(df_dog['Close'].pct_change(), label='Percentage Change Daily')
        plt.legend()
        steps=550
        plt.xticks(df_dog.index[0::steps], fontsize=10)
        st.write(fig)

    with st.expander("Correlation Between All 3 Coins"):
        fig, ax = plt.subplots()
        sns.heatmap(df_close3.corr(), ax=ax, annot=True)
        st.write(fig)

    with st.expander("Google Trend - 5 Years"):
        st.line_chart(google_trend_5y.bitcoin)

    with st.expander("Google Trend - 3 Months Apr-Jul, 2021"):
        st.line_chart(google_trend_3m.bitcoin)

    with st.expander("Readdit Sentiment - 3 Months Apr-Jul, 2021"):
        st.line_chart(readdit_3m.daily_avg_polarity)

    with st.expander("Price & Readdit Daily Sentiment Apr-Jul, 2021"):
        st.line_chart(btc_price_polarity_trend.daily_avg_polarity)
        st.line_chart(btc_price_polarity_trend.Close)

    with st.expander("Price & Google Trend Apr-Jul, 2021"):
        st.line_chart(btc_price_polarity_trend.Close)
        st.line_chart(btc_price_polarity_trend.bitcoin)




#x = st.sidebar.slider('x') #slider - basic
#st.sidebar.write(x, 'squared is', x*x) #slider output

# selectbox with dropdown
#add_selectbox = st.sidebar.selectbox(
#    "How would you liek to be contacted?",
#    ('Email', 'Home phone', 'Mobile phone')
#)

# slider with title and option
#add_slider = st.sidebar.slider(
#    "select a range of values",
#    0.0, 100.0, (25.0, 75.0)
#)

# columns
#left_column, right_column = st.columns(2)
#left_column.button('Press me!')

#with right_column:
#    chosen = st.radio(
#        "sorting hat",
#        ("gryffindor", "ravenclaw", "hufflepuff", "slytherin"))
#    st.write(f"you are in {chosen} house!")


#st.text_input("Your name", key="name")
#st.session_state.name

#git push origin master
"""
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.73:8501

"""

"""
Markdown cheatsheet
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
"""