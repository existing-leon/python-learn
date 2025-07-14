import yfinance as yf
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')  # 更换为 TkAgg 后端
import matplotlib.pyplot as plt

'''
回测是在历史市场数据上模拟和评估一个交易策略的过程。
以下是一个简单的移动平均交叉策略回测的实例代码，策略是在 50 日均线上穿越 200 日均线时买入，下穿越时卖出，策略的表现输出了总收益、年化收益和最大回撤等指标。
'''

# 获取股票数据
symbol = "603305.SS"
start_date = "2024-01-01"
end_date = "2025-03-10"

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# 初始化交叉信号列
data['Signal'] = 0

# 计算交叉信号
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1

# 计算每日收益率
data['Daily_Return'] = data['Close'].pct_change()

# 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

# 计算累计收益
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

# 输出策略表现
strategy_performance = {
    'Total Return': data['Cumulative_Return'].iloc[-1] - 1,
    'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1,
    'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min(),
}

print("策略表现:")
for key, value in strategy_performance.items():
    print(f"{key}: {value:.4f}")

# 绘制累计收益曲线
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()
