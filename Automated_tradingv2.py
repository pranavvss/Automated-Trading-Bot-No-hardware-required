import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD
from ta.volatility import BollingerBands, AverageTrueRange
import ccxt

def fetch_data(ticker, start_date="2015-01-01", end_date="2023-01-01"):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def apply_advanced_strategy(data):
    rsi = RSIIndicator(close=data['Close'], window=14)
    data['RSI'] = rsi.rsi()

    macd = MACD(close=data['Close'], window_slow=26, window_fast=12, window_sign=9)
    data['MACD'] = macd.macd()
    data['MACD_Signal'] = macd.macd_signal()

    bb = BollingerBands(close=data['Close'], window=20, window_dev=2)
    data['BB_Upper'] = bb.bollinger_hband()
    data['BB_Lower'] = bb.bollinger_lband()

    stoch = StochasticOscillator(high=data['High'], low=data['Low'], close=data['Close'], window=14, smooth_window=3)
    data['Stoch_K'] = stoch.stoch()
    data['Stoch_D'] = stoch.stoch_signal()

    return data

def generate_signals(data):
    data['Buy_Signal'] = ((data['RSI'] < 30) & 
                          (data['MACD'] > data['MACD_Signal']) & 
                          (data['Close'] < data['BB_Lower'])).astype(int)
    
    data['Sell_Signal'] = ((data['RSI'] > 70) & 
                           (data['MACD'] < data['MACD_Signal']) & 
                           (data['Close'] > data['BB_Upper'])).astype(int)
    
    return data

def calculate_position_size(data, balance, risk_per_trade=0.02):
    atr = AverageTrueRange(high=data['High'], low=data['Low'], close=data['Close'], window=14)
    data['ATR'] = atr.average_true_range()

    data['Position_Size'] = balance * risk_per_trade / data['ATR']

    return data

def backtest_advanced_strategy(data, initial_balance=10000, risk_per_trade=0.02):
    balance = initial_balance
    position = 0
    for i in range(1, len(data)):
        if data['Buy_Signal'].iloc[i] and position == 0:
            position_size = balance * risk_per_trade / data['ATR'].iloc[i]
            position = position_size / data['Close'].iloc[i]
            balance -= position_size
        
        elif data['Sell_Signal'].iloc[i] and position > 0:
            balance += position * data['Close'].iloc[i]
            position = 0

    if position > 0:
        balance += position * data['Close'].iloc[-1]

    return balance

def automate_advanced_trading(api_key, api_secret, data, risk_per_trade=0.02):
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
    })

    balance = 10000
    position = 0
    
    for i in range(1, len(data)):
        if data['Buy_Signal'].iloc[i] and position == 0:
            position_size = balance * risk_per_trade / data['ATR'].iloc[i]
            order = exchange.create_market_buy_order('BTC/USDT', position_size / data['Close'].iloc[i])
            position = order['amount']
            balance -= order['cost']
        
        elif data['Sell_Signal'].iloc[i] and position > 0:
            order = exchange.create_market_sell_order('BTC/USDT', position)
            balance += order['cost']
            position = 0

    return balance

if __name__ == "__main__":
    data = fetch_data('AAPL')
    data = apply_advanced_strategy(data)
    data = generate_signals(data)
    data = calculate_position_size(data, 10000)
    final_balance = backtest_advanced_strategy(data)
    print(f"Final balance after backtesting: ${final_balance:.2f}")
    
    automate_advanced_trading('paste_your_api_key', 'paste_your_api_secret', data)
