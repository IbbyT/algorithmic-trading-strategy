# Algorithmic Trading Strategy

## Overview

This project implements a simple algorithmic trading strategy using moving averages, stop-loss, and take-profit rules. The strategy is based on two Simple Moving Averages (SMAs) and generates buy and sell signals for the stock ticker symbol 'META' using historical data from Yahoo Finance.

## Features

- **Moving Averages**: Uses two SMAs with configurable periods to generate trading signals.
- **Buy/Sell Signals**: Identifies buy and sell signals based on the crossover of SMAs.
- **Risk Management**: Implements stop-loss and take-profit mechanisms to manage risk.
- **Performance Metrics**: Calculates and displays total return, Sharpe ratio, and maximum drawdown.
- **Visualization**: Plots share price, SMAs, and buy/sell signals.

## Installation

To run this project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/algorithmic-trading-strategy.git
   cd algorithmic-trading-strategy

2. **Install the required packages**
   ```bash
   pip install yfinance numpy matplotlib

## Usage
1. **Run the Script**
   ```bash
   python algorithmic_trading_strategy.py
2. **Review the Output**
   - The script will print a summary of performance metrics including total trades, total return, Sharpe ratio, and maximum drawdown.
   - A plot will be displayed showing the share price, SMAs, and buy/sell signals.

## Parameters
**Moving Average Periods:**
   - ma_1: Period for the shorter-term SMA (default: 30).
   - ma_2: Period for the longer-term SMA (default: 100).
**Risk Management:**
  - stop_loss_pct: Stop-loss percentage (default: 2%).
  - take_profit_pct: Take-profit percentage (default: 5%).

## Results
**After running the script, the following results will be displayed:**
- Total Trades: The number of buy/sell trades executed.
- Total Return: The cumulative return from the trading strategy.
- Sharpe Ratio: A measure of the risk-adjusted return.
- Max Drawdown: The maximum observed loss from a peak to a trough.
