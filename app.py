import streamlit as st

# from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
import os

import pandas as pd
from model import get_price_prediction_model
from bot import get_crypto_trading

# load the Environment Variables. 
load_dotenv()
st.set_page_config(page_title="Amazon Product App")

# Access environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

#api_key = os.environ.get(api_key)
#api_secret = os.environ.get(api_secret)

# Sidebar contents
with st.sidebar:
    st.title('Cryptocurrency Price Prediction 📈🤗')
    st.markdown('''
    ## About
    This web-app is an cryptocurrrency price prediction and trading bot based on binance API.
    ''')

    st.write('Made by [Harshil Agrawal](https://github.com/Harshil-Agrawal)')

st.header("Cryptocurrency Price Prediction 📈")
st.divider()

def main():

    st.subheader("Predict future date price: ")
    with st.form(key='my_form'):
        date=st.date_input('Enter the date')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.info("Predicted Price (USD):")
        # answer = get_price_prediction_model('2023-08-16')
        answer = get_price_prediction_model(date)
        st.write(answer)

        if answer:
            # Bot crypto trading
            st.subheader("Trading bot 🤖: ")
            with st.form(key='my_form_bot'):
                signal, sma_short, sma_long, buy_signal, sell_signal = get_crypto_trading(api_key, api_secret)
                st.write(signal)
                st.write("Short SMA:", sma_short)
                st.write("Long SMA:", sma_long)
                st.write("Buy signal:", buy_signal)
                st.write("Sell signal:", sell_signal)
                okay_button = st.form_submit_button(label='Okay')
    # st.divider()

print(api_key,api_secret)

if __name__ == '__main__':
    main()
