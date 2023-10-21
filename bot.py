import os
import ccxt  # Crypto exchange library
import numpy as np
from dotenv import load_dotenv
import requests

def get_crypto_trading():
        
    symbol = 'BTC/USDT'
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

    # Calculate SMAs
    sma_short = np.mean(close_prices[-sma_period_short:])
    sma_long = np.mean(close_prices[-sma_period_long:])

    # Determine Buy/Sell signals
    buy_signal = sma_short > sma_long
    sell_signal = sma_short < sma_long

    # Simulated trading logic (CryptoCompare does not support trading)
    if buy_signal:
        signal = "Buy signal detected. Execute buy order (simulated)."

    if sell_signal:
        signal = "Sell signal detected. Execute sell order (simulated)."    
    
    return signal, sma_short, sma_long, buy_signal, sell_signal

# Display trading signals
# print("Short SMA:", sma_short)
# print("Long SMA:", sma_long)
# print("Buy signal:", buy_signal)
# print("Sell signal:", sell_signal)
