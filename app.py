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


#api_key = os.environ.get(api_key)
#api_secret = os.environ.get(api_secret)

#  Sidebar contents 
with st.sidebar:
    st.image("CryptoGuides.png")
    st.divider()
    st.markdown('''
    ## About
    This is a cryptocurrrency price prediction and Crypto trading bot web-app.
    ''')


st.title("Cryptocurrency Price Prediction 📈 and Trading Bot 🤖")
st.divider()

def main():
    
    option = st.selectbox("Choose one", ["Currency Price Prediction", "Crypto Trading Bot"])

    if option == "Currency Price Prediction":
        #tab1, tab2 = st.tabs(["Currency Price Prediction", "Crypto Trading Bot"])

        st.subheader("Predict future date price: ")
        with st.form(key='my_form'):
            date=st.date_input('Enter the date')
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                st.info("Predicted Price (USD):")
                # answer = get_price_prediction_model('2023-08-16')
                answer = get_price_prediction_model(date)
                P_BTC = answer["Bitcoin"]
                P_ETH = answer["Ethereum"] 
                P_LTC = answer["Litecoin"]  
                st.write("Price of Bitcoin: ",P_BTC)
                st.write("Price of Ethereum: ",P_ETH)
                st.write("Price of Litecoin: ",P_LTC)
                okay_button = st.form_submit_button(label='Okay')

    if option == "Crypto Trading Bot":
        tab1, tab2, tab3 = st.tabs(["Bitcoin", "Ethereum","Litecoin"])

        # Bot crypto trading
        with tab1:
            st.subheader("Trading bot 🤖: ")
            with st.form(key='my_form_bot'):
                date=st.date_input('Enter the date')
                submit_button_2 = st.form_submit_button(label='Submit')

                if submit_button_2:

                    signal, sma_short, sma_long = get_crypto_trading(date,'BTC/USDT')
                    st.write(signal)
                    st.write("Short SMA:", sma_short)
                    st.write("Long SMA:", sma_long)
                    okay_button = st.form_submit_button(label='Okay')

        with tab2:
            st.subheader("Trading bot 🤖: ")
            with st.form(key='my_form_bot_2'):
                date=st.date_input('Enter the date')
                submit_button_2 = st.form_submit_button(label='Submit')

                if submit_button_2:

                    signal, sma_short, sma_long = get_crypto_trading(date,'ETH/USDT')
                    st.write(signal)
                    st.write("Short SMA:", sma_short)
                    st.write("Long SMA:", sma_long)
                    okay_button = st.form_submit_button(label='Okay')     
        
        with tab3:
            st.subheader("Trading bot 🤖: ")
            with st.form(key='my_form_bot_3'):
                date=st.date_input('Enter the date')
                submit_button_2 = st.form_submit_button(label='Submit')

                if submit_button_2:

                    signal, sma_short, sma_long = get_crypto_trading(date,'LTC/USDT')
                    st.write(signal)
                    st.write("Short SMA:", sma_short)
                    st.write("Long SMA:", sma_long)
                    okay_button = st.form_submit_button(label='Okay')     
    # st.divider()

if __name__ == '__main__':
    main()
