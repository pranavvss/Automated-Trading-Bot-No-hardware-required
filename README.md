# Automated-Trading-Bot-No-hardware-required-

## Requirements
1. Programming Language- Python: The bot is implemented in Python which is ideal for data analysis, algorithmic trading, and automation tasks.
2 Python Libraries - pandas, numpy, matplotlib(Optional), yfinance, ta, ccxt
3 Tools and Environment - Python Interpreter or Any Ide (For eg. Visual Studio Code or PyCharm)
4. Cloud Service (Optional): AWS EC2, Google Cloud to deploy the bot for 24/7 operation. (If preffer AWS, it is free for 1 year with new gmail account)
5. API Keys: If deploying live, you will need API keys from a cryptocurrency exchange like Binance or Coinbase or any other to execute trades.

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


