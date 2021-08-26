## Executive Summary

### Overview
During the COVID-19 pandemic, the news of cryptocurrency has emerged as this new safe heaven to put your cash in for better investment return as well as against inflation. Cryptocurrencies, in general, have increased as much as 100-times during the last 5 year. Specifically, the mother of all cryptocurrencies - Bitcoin - has increased from a low of $600 in 2017 to highest point of $61,000 in 2021 April. The price movement of the coins and the online buzz of cryptocurrency have significantly increased for retail investors. Hence, the phenomenon is worth our time to investigate for data scientists and retail investors such as myself. 

In this presentation, we will explore the following:
1. Correlation between the top 3 cryptocurrencies by market cap, and an additional meme crypto
2. Time series Bitcoin price prediction base on time lags
3. Public Sentiment on social media, namely Readdit subforum, and Google trend
4. Time series Bitcoin price prediction with time lags AND sentiment analysis of social media posts with google trend


### Problem Statement

The goal of my first capstone aims to create a crypto investment app to serve as an additional input with the insight of public sentiment of a given cryptocurrency to everyday retail investors. In order to better understand the price movement of cryptocurrencies, we'll explore the above data and proof myself (and many others) wrong that public sentiment on social media has little to do with the bull price movement we saw during the start of COVID-19 pandemic, regardless of what we naively believe in. 

A good portion of this project is spent on data wrangling, cleaning, and processing while the last part is dedicated to model training and predictions. 

The key deliverable from this project is a tool that scrapes thousands of Reddit posts on Bitcoin (r/bitcoin) in combination of google trend to analyze and model the relationships between daily closing price and public sentiment from April 7 to July 6, 2021 (3 months trend).

Viewer can acess to the web-app [here] (https://cryptosentiment.herojuapp.com/)


### Contents of this README

- Executive Summary
- Data-set Description
- Primary Findings and Insights
- Conclusion & Recommendations
- Next Steps


### Data-set Description

#### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|date|datetime64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|High|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|Low|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|Open|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|Close|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|Marketcap|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|Close_7days|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|daily_avg_polarity|float64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|bitcoin|int64|btc_price_polarity_trend.csv|Daily historical trend of bitcoin price with average polarity of given day's readdit post under subreaddit forum r/bitcoin, and daily google trend of keyword 'bitcoin' from April 7-July 6, 2021|
|date|datetime64|google_trend_5y.csv / google_trend_3m.csv|The date of the keyword search
|bitcoin|int64|google_trend_5y.csv / google_trend_3m.csv|number of keyword search on given cryptocurrency during the dat, or every 5 days on Google|
|crypto|int64|google_trend_5y.csv / google_trend_3m.csv|number of keyword search on given cryptocurrency during the dat, or every 5 days on Google|
|etherum|int64|google_trend_5y.csv / google_trend_3m.csv|number of keyword search on given cryptocurrency during the dat, or every 5 days on Google|
|cardano|int64|google_trend_5y.csv / google_trend_3m.csv|number of keyword search on given cryptocurrency during the dat, or every 5 days on Google|
|dogecoin|int64|google_trend_5y.csv / google_trend_3m.csv|number of keyword search on given cryptocurrency during the dat, or every 5 days on Google|
|isPartial|int64|google_trend_5y.csv / google_trend_3m.csv|TRUE/FALSE means when they API is used or not|
|created_utc|int64|readdit_btc.csv|The UTC time when the readdit post was first originally created and posted on to the given subreaddit forum|
|subreaddit|object|readdit_btc.csv|The name of the subreaddit forum|
|text|object|readdit_btc.csv|The entire text of the given subreaddit post|

### Requirements
- Python 3.8.5
- Pandas
- Numpy
- Matplotlib
- Datetime
- Pytrend
- Tensorflow
- Tweepy
- Statsmodels
- Seaborn
- Scikit_learn
- Requests
- Json
- Pandas_datareader.data
- NLTK
- Textblob
- Pickle


#### Provided Data and Workbooks
For this capstone project, the following Jupyter notebooks are used:
- [EDA - Load and Clean](/Capstone1_1_Load_and_Clean.ipynb)
    - Data In:
        - Kaggle Data (https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory)
            - Bitcoin (cryptodata/coin_Bitcoin.csv)
            - Ethereum (cryptodata/coin_Ethereum.csv)
            - Cardano (cryptodata/coin_Cardano.csv)
            - Dogecoin (cryptodata/coin_Dogecoin.csv)
    - Data Out:
        - Cleaned Data
            - Bitcoin (cryptodata/cleaned_btc.csv)
            - Ethereum (cryptodata/cleaned_eth.csv)
            - Cardano (cryptodata/cleaned_ada.csv)
            - Dogecoin (cryptodata/cleaned_dog.csv)
            - Correlation of all 4 coins (cryptodata/3coinsclose.csv)
- [Scrapping Twitter Data](/Capstone1_2_ScrapeTwitter.ipynb)
    - Data In:
        - Twitter API
    - Data Out:
        - Most recent Bitcoin tweets (data/btc_df_complete.csv)
        - Most recent Ethereum tweets (data/eth_df_complete.csv)
        - Most recent Cardano tweets (data/ada_df_complete.csv)
        - Most recent Dogecoin tweets (data/dog_df_complete.csv)
        - Most recent cryptocurrency tweets (/data/all_crypto_tweets.csv)
- [Scrapping Readdit Data](/Capstone1_2.2_ScrapeReaddit.ipynb)
    - Data In:
        - Readdit API
    - Data Out:
        - 100 readdit posts of everyday between April 7 - July 6, 2021 (data/readdit_btc.csv)
- [Scrapping Google Trend](/Capstone1_2.3_ScrapeGoogleTrend.ipynb)
    - Data In:
        - Google API
    - Data Out:
        - Goolge Trend of past 5 years on 5 keywords by 5-Day Average (data/google_trend_5y.csv)
        - Google Trend of on 5 keywords by day between April 7 - July 6, 2021 (data/google_trend_3m.csv)
- [Sentiment Analysis](/Capstone1_3_SentimentAnalysis.ipynb)
    - Data In:
        - Bitcoin Historical Record (cryptodata/cleaned_btc.csv)
        - Readdit Posts by day (data/readdit_btc.csv)
        - 3 months Google Trend (data/google_trend_3m.csv)
    - Data Out:
        - Bitcoin Historical Record with Readdit Sentiment Analysis and Google trend (data/btc_price_polarity_trend.csv)
- [Time Series Price Prediction on BTC](/Capstone1_4_PricePrediction_BTC.ipynb)
    - Data In:
        - Bitcoin Historical Record (data/df_btc.csv)
    - Data Out:
        - Time Series Linear Model (assets/linear_model.csv)
- [Time Series Price Prediction with Sentiment Analysis and Google Trend](/Capstone1_4.2_PriceSentimentTrendPrediction_BTC.ipynb)
    - Data In:
        - 3 months Price Polarity based on subreaddit forum (data/df_3m_price_polarity.csv)
        - 3 months Price Polarity with Google Trend (data/btc_price_polarity_trend.csv)
    - Data Out:
        - 
- [Final Recommendation](/Capstone1_5_Recommendation.ipynb)
    - Data In:
        - Bitcoin Cleaned Historical Record (cryptodata/cleaned_btc.csv)
        - 3 months Price Polarity based on subreaddit forum (data/df_3m_price_polarity.csv)
        - 3 months Price Polarity with Google Trend (data/btc_price_polarity_trend.csv)
    - Data Out:

The following python files are used to build the web-app on Streamlit:
- [Main Page] (/main_page.py)
- [Price Prediction] (/price_pred.py)
- [Recommendation] (/recommendation.py)

### Primary Findings & Insights
From the initial EDA, we can see that there are strong correlation between Bitcoin, Ethereum, and Cardano, and mediocore correlation between these 3 and the meme coin Dogecoin in terms of closing price. Hence, it's safe to assume that whatever models we choose to use in the future can be used on the top 3 cryptocurrencies by marketcap. 

From the second stage of EDA, where I pulled the Google Trend data, we can see that the peaks of mentions of the keywords (bitcoin, crypto, ethereum, cardano, and dogecoin) all have similar peaked points, and the location of the peaked points look similar to graph of the closing price peaked points. Hence, in order to figure out if these trends are people talking negatively or positively about Bitcoin or not, we need some data on the public sentiment, and the best (and more convenient) way going about it is to see what people are talking about on Readdit forum (r/bitcoin). 

For the sentiment analysis, I aggregate the daily posts on r/bitcoin between April 7 and July 6, 2021, it appears that in general the sentiment are positive even though there are some negative sentiment posts everyday (49% of neutral sentiment, 41% positive sentiment, and 20% negative sentiment). So far it looks like we are on a good track.

In addition, I also put the daily closing price together with daily average polarity, and daily google trend number to find the correlation. The correlation between daily closing price and daily average polarity is at 9.98%, and the correlation between daily closing price and daily google trend is at 18.2%. The correlation between polarity and google trend is -10.6%.

For the training and model prediction part, I first trained and evluated both time series linear regression model and ARIMA. The linear regression model performance is at 0.996% for testing data, and 0.995% for training data for basic price prediction using autocrrelation (lag 1, lag 2, and lag 7). The ARIMA model on the other hand performs poorly. 

For price prediciton using autocorrelation (lag 1, 2, and 7) with daily polarity and polarity autocorrelation (plag1, plag2, plag7), the linear regression model peroformance drops significantly with a R2 score at -0.63 for testing data, and 0.954 for training data. The model is way too overfit. Once we add in google trend into the model, the R2 score drops even more to -1.11 for testing data, and 0.952 for training data. This explains about the correlation of -10.6% between readdit post polarity and google trend. 

However, one interesting fact to note is that the graph of price prediction between y_test and X_test do still have somewhat of a similar trend for both linear regression models.  


### Limitation 
Time constraint and data quantity were two of the biggest limitation of this project. In order to get a better sense of correlation between daily Readdit posts sentiment and daily Bitcoin closing price, the project would need more than 100 posts per day. However, the Readdit API only allows 100 posts per scrape. Hence, I'd need to put in more time and more codes to scrape more than 100 posts. If time allows, I'd scrape 500 posts minimum. 

Basic Twitter API has significant amount of limitation as they only allows you to scrape the latest 7 days tweets. Therefore, I was not able to get the tweets between April 7 and July 6 of this year. Hence, twitter was not used in this project at the end.

With more time, I think using google trend 5 years with closing price 5 years of bitcoin can give us a better picture than 3 months.


### Conclusion & Recommendations
The web-app that I built can be a valuable asset to regular retail investors like me to guide our assumption by providing numbers that are converted from the public's sentiment of a given cryptocurrency. This tool can be served to give investors a sense of reality and prevent us from making horrible financial investment decision. Regardless of what the bull market may appear to look like, in combination of what seemly are positive exposures on social media, the public sentiment of a given cryptocurrency does not, and should not, serve as a major reason of investment. Public sentiment should only be served as an additional insight. Given the weak correlation of social media posts and google trend, we cannot infer that social media (namely readdit posts) plays a significant role in driving up the prices of cryptocurrency during the COVID-19 pandemic. 

Predicting any time series event is exceptionally hard. In the case of predicting price of bitcoin, the best way is to use time series linear model to predict the price lag of yesterday, the day before yesterday, and the seasonal trend. Given that the model is performing at 99.5% for testing data, any other features I'm adding such as public sentiments are just adding noises.

That being said, this tool should only be served as an additional insight to what the public is thinking, as well as doubling checking of your beliefs with realistic data and numbers (i.e. updating your beliefs). It is appearent that the public, sometimes, does not act based on what they post. 

### Next Steps
For next steps, I'd recommend to use 2 additional stocks to put as an additional insight to cryptocurrency price prediction. The 2 stocks are AMD and NVIDIA. These two stocks are semiconductor companies that make the semiconductors to use for coin mining. There are many more ideas to improve the workability, efficiency, and usefulness of this application from its current intial prototype.

Futhermore, I'd also recommend to bring this web-app to come to life by giving a minimalistic user design. Working with one UX designer and software engineer are essential to bring this valuable app to life. 

Thank you!
