import streamlit as st
import time
import numpy as np
import pandas as pd
import altair as lt
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, datetime
import pickle
import statsmodels.api as sm



def app():
    st.write(""" ### Price Predictions with Sentimental Analysis """)

    # Load data
    df = pd.read_csv('data/btc_price_polarity_trend.csv')
    df_s = pd.read_csv('data/reddit_btc_roll.csv')
    df_g = pd.read_csv('data/google_trend_3m.csv')


    # Collects user features into dataframe

    # set up parameters
    #def user_input_features():
    start_date = st.date_input('Start Date', min_value=(datetime(2021, 4, 7)), max_value=(datetime(2021, 7, 6)))
    end_date = st.date_input('End Date', min_value=(datetime(2021, 4, 7)), max_value=(datetime(2021, 7, 6))) 
    closing_price = st.slider('Closing Price', 600,60000,)
    data = {'start_date': start_date,
            'end_date': end_date,
            'Closing Price': closing_price}
    features = pd.DataFrame(data, index=[0])
    #return features
    #input_df = user_input_features()

    # Correlation
    
    with st.expander(f'Correlation BTC {start_date} - {end_date}'):
        corr_pg = round(df['Close'].corr(df['bitcoin']), 4)*100
        corr_pr = round(df['Close'].corr(df['daily_avg_polarity']), 4)*100
        corr_gr = round(df['bitcoin'].corr(df['daily_avg_polarity']), 4)
        df_ppt = df.drop(columns=['High', 'Low', 'Open', 'Marketcap', 'Close_7days'])

        # create grid
        col1, col2 = st.columns((1.9, 1.4))
        col1.write('')
        col1.write('')
        col1.write(f'Correlation Price & Google Trend: {corr_pg} %')
        col1.write('')
        col1.write('')
        col1.write(f'Correlation Price & Reddit Sentiment: {corr_pr} %')
        fig, ax = plt.subplots()
        sns.heatmap(df_ppt.corr(), ax=ax, annot=True)
        col2.write(fig)
        st.write(' ')
        st.write(' ')
        st.write(' ')

    # Reddit Sentiment 
    with st.expander(f'Reddit Sentiment Analysis {start_date} - {end_date}'):
        st.write('')
        st.write('Daily Sentiment is the average of the sentiment top 100 Reddit posts.')
        sentiment = round(df_s['polarity'].mean(), 4)*100
        st.write(f'Average Sentiment between {start_date} - {end_date} is: {sentiment} %')
        if sentiment > 0:
            sentiment_state = 'Positive'
        else:
            sentiment_state = 'Negative'
        st.write(f'Overall Sentiment: {sentiment_state}')
        col3, col4 = st.columns((1.9, 1.4))
        col3.write('#### Scatter Plot of Sentiment')
        col3.write('X-axis shown in UTC time')
        fig1 = plt.figure(figsize=(12, 9))
        plt.scatter(df_s['created_utc'], df_s['polarity'])
        plt.show()
        col3.write(fig1)
        col4.write('#### Line Chart of Sentiment')
        col4.write('X-axis shown in UTC time')
        fig2 = plt.figure(figsize=(12, 9))
        plt.plot(df_s['created_utc'], df_s['rolling_200'])
        plt.show()
        col4.write(fig2)

    # Google Trend
    with st.expander(f'Google Trend {start_date} - {end_date}'):
        fig3 = plt.figure(figsize=(12, 9))
        plt.plot(df_g.index, df_g['bitcoin'], label='bitcoin')
        plt.plot(df_g.index, df_g['crypto'], label='crypto')
        plt.plot(df_g.index, df_g['ethereum'], label='ethereum')
        plt.plot(df_g.index, df_g['cardano'], label='cardano')
        plt.plot(df_g.index, df_g['dogecoin'], label='dogecoin')
        plt.legend(loc="upper left")
        st.write(fig3)    

     # Price Prediction
    with st.expander('Price Predictions for the next 7 days'):

        # Reads in saved model
        filename = 'assets/linear_model.pkl'
        loaded_model = pickle.load(open(filename, 'rb'))

        # Apply model to make predictions
        #preds = loaded_model.predict(df)

        #price = 
        st.write(price[preds])

