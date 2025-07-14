import yfinance as yf
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')  # 更换为 TkAgg 后端
import matplotlib.pyplot as plt

'''
使用 pandas 进行数据分析和 matplotlib 进行可视化
'''

# 获取股票数据
symbol = "603305.SS"
start_date = "2024-01-01"
end_date = "2025-03-10"

data = yf.download(symbol, start=start_date, end=end_date)
# 简单的数据分析
print(data.describe())

# 绘制股价走势图
data['Close'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
