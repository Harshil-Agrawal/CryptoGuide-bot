import os
import ccxt  # Crypto exchange library
import numpy as np
from dotenv import load_dotenv
import requests
import talib
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def get_crypto_trading(date,crypto):
        

    # Constants
    symbol = crypto #'BTC/USDT'
    timeframe = 'hour'  # CryptoCompare uses 'minute', 'hour', or 'day' for timeframe
    sma_period_short = 50
    sma_period_long = 200

    # Fetch historical data from CryptoCompare
    url = f"https://min-api.cryptocompare.com/data/v2/histohour?fsym={symbol.split('/')[0]}&tsym={symbol.split('/')[1]}&limit=1000&e=binance"
    response = requests.get(url)
    data = response.json()
    ohlcv = data['Data']['Data']

    # Extract timestamps and close prices
    timestamps = [entry['time'] for entry in ohlcv]
    close_prices = [entry['close'] for entry in ohlcv]

    # Create a DataFrame for easier handling of data
    df = pd.DataFrame({'timestamp': timestamps, 'close': close_prices})
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)

    # Calculate SMAs using Ta-Lib
    df['sma_short'] = talib.SMA(df['close'].values, timeperiod=sma_period_short)
    df['sma_long'] = talib.SMA(df['close'].values, timeperiod=sma_period_long)

    # Determine Buy/Sell signals based on SMAs
    df['buy_signal'] = np.where(df['sma_short'] > df['sma_long'], 1, 0)
    df['sell_signal'] = np.where(df['sma_short'] < df['sma_long'], 1, 0)

    # Drop NaN values introduced by SMA calculation
    df.dropna(inplace=True)

    # Use SARIMAX to predict Buy/Hold/Sell for a specific future date

    # Fit SARIMAX model
    X = df[['sma_short', 'sma_long']]
    y = df['close']

    model = SARIMAX(y, exog=X, order=(1, 1, 1), seasonal_order=(1, 1, 1, 24))
    sarimax_results = model.fit(disp=False)

    # Prediction for a specific future date
    future_date = pd.to_datetime(date)
    future_data = X.tail(1)  # Use the last row of X as exog for prediction
    prediction = sarimax_results.get_forecast(steps=1, exog=future_data)

    # Get the predicted value
    predicted_price = prediction.predicted_mean[0]

    # Determine Buy/Hold/Sell based on predicted value
    if predicted_price > df['close'].iloc[-1]:
        signal = "Buy signal predicted for the given date."
    elif predicted_price < df['close'].iloc[-1]:
        signal = "Sell signal predicted for the given date."
    else:
        signal = "Hold signal predicted for the given date."

    sma_short = df['sma_short'].iloc[-1]
    sma_long = df['sma_long'].iloc[-1]

        
    return signal, sma_short, sma_long

# Display trading signals
# print("Short SMA:", sma_short)
# print("Long SMA:", sma_long)
# print("Buy signal:", buy_signal)
# print("Sell signal:", sell_signal)
