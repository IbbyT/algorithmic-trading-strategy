#algorithmic trading strategy
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

plt.style.use("dark_background")

#parameters
ma_1 = 30
ma_2 = 100
stop_loss_pct = 0.02  # 2% stop loss
take_profit_pct = 0.05  # 5% take profit

start = dt.datetime.now() - dt.timedelta(days=365 * 3)
end = dt.datetime.now()

#fetching data
data = yf.download('META', start=start, end=end)
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window=ma_1).mean()
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window=ma_2).mean()

#cutting data for NaN values
data = data.iloc[ma_2:]

#generate buy/sell signals
buy_signals = []
sell_signals = []
trigger = 0  
buy_price = 0
total_return = 0
trades = 0

#list for returns
returns = []

for x in range(len(data)):
    price = data['Adj Close'].iloc[x]
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and trigger != 1:
        #buy signal
        buy_signals.append(price)
        sell_signals.append(float('nan'))
        trigger = 1
        buy_price = price
        trades += 1
    elif data[f'SMA_{ma_1}'].iloc[x] < data[f'SMA_{ma_2}'].iloc[x] and trigger == 1:
        #sell signal
        buy_signals.append(float('nan'))
        sell_signals.append(price)
        trade_return = (price - buy_price) / buy_price
        total_return += trade_return
        returns.append(trade_return)
        trigger = -1
    else:
        #hold, stop-loss and take-profit management
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))
        if trigger == 1:  # Check if a position is open
            if (price - buy_price) / buy_price <= -stop_loss_pct:  # Stop-loss triggered
                sell_signals[-1] = price
                total_return += -stop_loss_pct
                returns.append(-stop_loss_pct)
                trigger = -1
            elif (price - buy_price) / buy_price >= take_profit_pct:  # Take-profit triggered
                sell_signals[-1] = price
                total_return += take_profit_pct
                returns.append(take_profit_pct)
                trigger = -1

data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals

#performance metrics
sharpe_ratio = (np.mean(returns) / np.std(returns)) * np.sqrt(252) if len(returns) > 0 else 0
max_drawdown = min(returns) if len(returns) > 0 else 0

#display summary of performance
print(f"Total Trades: {trades}")
print(f"Total Return: {total_return * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown * 100:.2f}%")

#plotting share price, SMAs, and buy/sell signals
plt.plot(data['Adj Close'], label="Share Price", alpha=0.5)
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange", linestyle='--')
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="pink", linestyle="--")

#buy/sell signals with scatter plot
plt.scatter(data.index, data['Buy Signals'], label="Buy Signal", marker="^", color="#00ff00", lw=3)
plt.scatter(data.index, data['Sell Signals'], label="Sell Signal", marker="v", color="#ff0000", lw=3)

plt.legend(loc="upper left")
plt.title(f"Algorithmic Trading Strategy with {ma_1}/{ma_2} SMAs, Sharpe Ratio: {sharpe_ratio:.2f}, Total Return: {total_return*100:.2f}%")
plt.show()
