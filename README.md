# Automated-Trading-Bot-No-hardware-required- 

This automated trading bot provides a advance framework for algorithmic trading, utilizing advanced technical indicators and a carefully designed strategy. This document by me serves as a guide for understanding and setting up the bot, ensuring it runs efficiently in a live trading environment. This Document is not for beginners, You need to have good knowledge of python atleast and you can ready the documents of all the libraries mentioned below.

<img src="https://github.com/user-attachments/assets/ce63ac01-8343-413e-83c9-143378cd49a6" width="300" />


---------------------------------------------------------------------
# Warning
It is not recommended to use this bot on real money. Any loss won't be counted as my fault. This project is made to help me grow my knowledge as well as share a structured document for others to understand how automated trading work. I highly recommend to only use Fake money to test this bot (Paper trading).
---------------------------------------------------------------------

## Requirements
1. Programming Language- Python: The bot is implemented in Python which is ideal for data analysis, algorithmic trading, and automation tasks.
2 Python Libraries
- [pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
- [numpy](https://numpy.org/devdocs/user/absolute_beginners.html)
- [matplotlib(Optional)](https://numpy.org/devdocs/user/absolute_beginners.html)
- [yfinance or Yahoo Finance](https://algotrading101.com/learn/yfinance-guide/)
- [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)
- [ccxt](https://docs.ccxt.com/#/)
  
or If you want to trade in forex(as markets are always open) ccxt can be used too but fxcmpy is better in my knowledge. 

- [fxcmpy](https://fxcm-api.readthedocs.io/en/latest/)

Read all the documents if you are not familiar with their workings.
  
3. Tools and Environment - Python Interpreter or Any Ide (For eg. Visual Studio Code or PyCharm)
4. Cloud Service (Optional): AWS EC2, Google Cloud to deploy the bot for 24/7 operation. (If preffer AWS, it is free for 1 year with new gmail account)
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
