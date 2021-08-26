import streamlit as st
import main_page
import price_pred


# Sidebar Selection

PAGES = {
    'Main Page': main_page,
    'Price Prediction with Sentimental Analysis': price_pred
}


st.sidebar.title('CryptoSentiment')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

page.app()
