# Automated-Trading-Bot-No-hardware-required 

This automated trading bot provides a advance framework for algorithmic trading, utilizing advanced technical indicators and a carefully designed strategy. This document by me serves as a guide for understanding and setting up the bot, ensuring it runs efficiently in a live trading environment. This Document is not for beginners, You need to have good knowledge of python atleast and you can ready the documents of all the libraries mentioned below. 

Below is a chart showing how we will proceed- 

<img src="https://github.com/user-attachments/assets/ce63ac01-8343-413e-83c9-143378cd49a6" width="300" />

---------------------------------------------------------------------
## Warning

It is not recommended to use this bot on real money. Any loss won't be counted as my fault. This project is made to help me grow my knowledge as well as share a structured document for others to understand how automated trading work. I highly recommend to only use Fake money to test this bot (Paper trading).

---------------------------------------------------------------------

## Requirements
1. Programming Language- Python: The bot is implemented in Python which is ideal for data analysis, algorithmic trading, and automation tasks. 

2. Python Libraries
- [pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
- [numpy](https://numpy.org/devdocs/user/absolute_beginners.html)
- [matplotlib(Optional)](https://numpy.org/devdocs/user/absolute_beginners.html)
- [yfinance or Yahoo Finance](https://algotrading101.com/learn/yfinance-guide/)
- [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)
- [ccxt](https://docs.ccxt.com/#/)
  
or If you want to trade in forex(as markets are always open from Monday to Friday) ccxt can be used indeed but i prefer fxcmpy.

- [fxcmpy](https://fxcm-api.readthedocs.io/en/latest/)

Read all the documents if you are not familiar with their workings.
  
3. Tools and Environment - Python Interpreter or Any Ide (For eg. Visual Studio Code or PyCharm)
4. Cloud Service (Optional, If you want to host a bot that keeps running 24/7 youll need a Virtual machine): AWS EC2, Google Cloud to deploy the bot for 24/7 operation. (I preffer AWS, it is free for 1 year with new gmail account)
5. API Keys: If deploying live, you will need API keys from a cryptocurrency exchange like Binance or Coinbase or any other to execute trades.
---------------------------------------------------------------------

## Overview
1. Strategy-
The bot employs a multi-indicator strategy that combines several technical analysis tools to generate buy and sell signals. The main indicators used are: Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), Bollinger Bands and Stochastic Oscillator.

2. Algorithm - The bot’s algorithm is structured as follows:
- Data Collection: Historical price data is fetched using the yfinance library.
- Indicator Calculation: The bot calculates technical indicators like RSI, MACD, Bollinger Bands, and the Stochastic Oscillator.
- Signal Generation: Based on predefined thresholds and crossovers of these indicators, the bot generates buy and sell signals.
- Backtesting: The strategy is backtested on historical data to evaluate its effectiveness.
- Position Sizing: The bot dynamically sizes positions based on the volatility of the asset using the Average True Range (ATR).
- Execution: In a live trading environment, the bot uses the ccxt library to connect to a cryptocurrency exchange and execute trades based on the generated signals.
- Deployment: The bot can be deployed on a cloud service like AWS EC2 to run continuously, ensuring it operates 24/7.

---------------------------------------------------------------------

# STEPS (Full Guide Below)

---------------------------------------------------------------------
### Step 1. Set Up Your Development Environment 

1.1 Install python 3.x (i prefer 3.11), Install Your preferred ide (I like Visual Studio Code) further Open cmd and type the command to verify that python was installed.
```
python --version
```

1.2 Install Required Libraries, open your command prompt (cmd or terminal in your ide) and run following command to install all required libraies at one go.
```
pip install pandas numpy matplotlib yfinance ta ccxt
```
---------------------------------------------------------------------
### Step 2. Gathering Market Data 

2.1 Our trading bot will need Data of past years to analyze trends and generate a trading strategy, for which we are using yfinance)

2.2 The following code is used to fetch data 
```
import yfinance as yf
import pandas as pd

def fetch_data(ticker, start_date="2015-01-01", end_date="2023-01-01"):
    # Fetch historical data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Example usage
data = fetch_data('AAPL')
print(data.head())
```

Note:
You can change AAPL with your desired Crpto Currency with the start and end date data you want to gather (Remember add the Ticker symbol (Means if you want to trade in "USD COIN" then under fetch_data() you need to enter ticker symbol of "USD COIN" which is USDC.
```
For eg. data = fetch_data('USDC')
```
---------------------------------------------------------------------
### Step 3. Implementing the Trading Strategy

3.1 We will RSI, Relative Strength Index to measure the magnitude of recent price changes to find did traders overbuy or oversell, then MACD, Moving Average Convergence Divergence will reveal us the relationship b/w two moving average of this Crypto currency's price, We will also use Bollinger Bands to Set above and below levels, At last we'll compare closing price of this crypto currency to a range of price of a certain period using Stochastic Oscillator. 

3.2 The following code calculates these indicators for use in our strategy
```
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD
from ta.volatility import BollingerBands

def apply_advanced_strategy(data):
    # Calculate RSI
    rsi = RSIIndicator(close=data['Close'], window=14)
    data['RSI'] = rsi.rsi()

    # Calculate MACD
    macd = MACD(close=data['Close'], window_slow=26, window_fast=12, window_sign=9)
    data['MACD'] = macd.macd()
    data['MACD_Signal'] = macd.macd_signal()

    # Calculate Bollinger Bands
    bb = BollingerBands(close=data['Close'], window=20, window_dev=2)
    data['BB_Upper'] = bb.bollinger_hband()
    data['BB_Lower'] = bb.bollinger_lband()

    # Calculate Stochastic Oscillator
    stoch = StochasticOscillator(high=data['High'], low=data['Low'], close=data['Close'], window=14, smooth_window=3)
    data['Stoch_K'] = stoch.stoch()
    data['Stoch_D'] = stoch.stoch_signal()

    return data

# Example
data = apply_advanced_strategy(data)
print(data[['RSI', 'MACD', 'BB_Upper', 'BB_Lower', 'Stoch_K', 'Stoch_D']].tail())
```

3.3 Now we'll generate signals based on the combination of indicators
```
def generate_signals(data):
    # Buy when RSI < 30, MACD crosses above signal, and price is below lower Bollinger Band
    data['Buy_Signal'] = ((data['RSI'] < 30) & 
                          (data['MACD'] > data['MACD_Signal']) & 
                          (data['Close'] < data['BB_Lower'])).astype(int)
    
    # Sell when RSI > 70, MACD crosses below signal, and price is above upper Bollinger Band
    data['Sell_Signal'] = ((data['RSI'] > 70) & 
                           (data['MACD'] < data['MACD_Signal']) & 
                           (data['Close'] > data['BB_Upper'])).astype(int)
    
    return data

# Example 
data = generate_signals(data)
print(data[['Close', 'Buy_Signal', 'Sell_Signal']].tail())
```
---------------------------------------------------------------------

### Step 4. Implementing Risk Management (Will add a code which will tell the bot a limit) Risk Management is very important, so that we are utilize our resource in proper manner, and when the time is right.
- Risk management depends on individuals, How much person x can risk to loose can differ from person y.

4.1 Now we will calculate Position Size
 ``` 
from ta.volatility import AverageTrueRange

def calculate_position_size(data, balance, risk_per_trade=0.02):
    # Calculate ATR
    atr = AverageTrueRange(high=data['High'], low=data['Low'], close=data['Close'], window=14)
    data['ATR'] = atr.average_true_range()

    # Calculate position size based on ATR and risk per trade
    data['Position_Size'] = balance * risk_per_trade / data['ATR']

    return data

# Example 
initial_balance = 10000 
data = calculate_position_size(data, initial_balance)
print(data[['Close', 'ATR', 'Position_Size']].tail())
```
Note: Under paper trading you get around 100k INR or equivalent, we are taking out 10k INR as our initial balance and we will trade on this 10k INR.

---------------------------------------------------------------------
### Step 5. Backtesting the Strategy (Backtesting is the process of testing a trading strategy on historical data to see how it would have performed. It’s crucial to validate a strategy before deploying it in a live trading environment(Where real money is at stake.)

5.1 Following are the code we'll add for backtesting
``` 
def backtest_advanced_strategy(data, initial_balance=10000, risk_per_trade=0.02):
    balance = initial_balance
    position = 0  # 0: no position, >0: holding a long position
    for i in range(1, len(data)):
        if data['Buy_Signal'].iloc[i] and position == 0:
            # Calculate position size and buy
            position_size = balance * risk_per_trade / data['ATR'].iloc[i]
            position = position_size / data['Close'].iloc[i]
            balance -= position_size
        
        elif data['Sell_Signal'].iloc[i] and position > 0:
            # Sell the position
            balance += position * data['Close'].iloc[i]
            position = 0

    # If still holding position, sell at the last close
    if position > 0:
        balance += position * data['Close'].iloc[-1]

    return balance

# Example 
final_balance = backtest_advanced_strategy(data, initial_balance)
print(f"Final balance after backtesting: ${final_balance:.2f}")
```
---------------------------------------------------------------------

### Step 6. Automating the Trading Bot

6.1 Now we'll Connect to a Cryptocurrency Exchange
- Use the ccxt library to interact with exchanges like Binance, Coinbase, or others. Ensure that you have an account with API keys generated.

6.2 Code for automated trading
```
import ccxt

def automate_advanced_trading(api_key, api_secret, data, risk_per_trade=0.02):
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
    })

    balance = 10000  # Set an initial balance 
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

# final_balance = automate_advanced_trading('add_your_api_key', 'add_your_api_secret', data)
# print(f"Final balance after automated trading: ${final_balance:.2f}")

```
---------------------------------------------------------------------

### Step 7: Deploying the Bot on a Cloud Service (if you want the bot to run 24/7)

7.1 Choosing a Cloud Service, I prefer AWS.

7.2 Setting up our Virtual Machine
- Step 1: Create an AWS account and navigate to the EC2 Dashboard.
- Step 2: Launch an EC2 instance. Choose a free-tier eligible instance type (e.g., t2.micro) and an Amazon Machine Image (AMI) with Ubuntu or your preferred OS.
- Step 3: Configure security groups to allow SSH access (port 22) and optionally HTTP/HTTPS if you need web access.
- Step 4: Connect to your instance using SSH.
For example
```
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

7.3 Installing Python and Libraries on the Cloud Server
```
sudo apt update
sudo apt install python3-pip
pip3 install pandas numpy matplotlib yfinance ta ccxt
```

7.4  Upload Your Code to the Cloud
```
scp -i your-key.pem pr_bot.py ubuntu@your-ec2-public-ip:~/
```

7.5 Running the Bot (Go to your bot’s directory and run the script)
```
python3 pr_bot.py
```
To keep the bot running 24/7, you can use screen or tmux
```
sudo apt install screen
screen -S trading_bot
python3 pr_bot.py
```

Your Bot will continously run in background now.

7.6 Setting Up Monitoring (To keep an eye on the bot's activity) 
Use monitoring tools like CloudWatch (AWS), Stackdriver (GCP), or simple logging to monitor the bot’s performance and errors.


---We are done-------------------------------------------------------------------------

---Please trade on paper tarding(Fake Money)-------------------------------------------

---Use real Money to trade with this bot on your own risk.-----------------------------

---This is posted only for education purpose and should be used for that only.---------
