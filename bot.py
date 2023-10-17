import os
import ccxt  # Crypto exchange library
import numpy as np
from dotenv import load_dotenv


def get_crypto_trading(api_key, api_secret):
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
    })

    # Constants
    symbol = 'BTC/USDT'
    timeframe = '1h'
    sma_period_short = 50
    sma_period_long = 200

    # Fetch historical data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    timestamps = [entry[0] for entry in ohlcv]
    close_prices = [entry[4] for entry in ohlcv]

    # Calculate SMAs
    sma_short = np.mean(close_prices[-sma_period_short:])
    sma_long = np.mean(close_prices[-sma_period_long:])

    # Determine Buy/Sell signals
    buy_signal = sma_short > sma_long
    sell_signal = sma_short < sma_long

    # Simulated trading logic
    if buy_signal:
        # print("Buy signal detected. Execute buy order.")
        signal = "Buy signal detected. Execute buy order."
        # Place buy order using the exchange API

    if sell_signal:
        # print("Sell signal detected. Execute sell order.")
        signal = "Sell signal detected. Execute sell order."
        # Place sell order using the exchange API
    
    return signal, sma_short, sma_long, buy_signal, sell_signal

# Display trading signals
# print("Short SMA:", sma_short)
# print("Long SMA:", sma_long)
# print("Buy signal:", buy_signal)
# print("Sell signal:", sell_signal)
