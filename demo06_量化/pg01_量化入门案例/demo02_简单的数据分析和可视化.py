import matplotlib
import yfinance as yf
import pandas as pd
matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt


# 获取旭升集团股票数据
symbol = "603305.SS"
start_date = "2024-01-01"
end_date = "2025-03-17"

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
