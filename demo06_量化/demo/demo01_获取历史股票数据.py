import yfinance as yf

'''
使用 yfinance 获取历史股票数据
'''

# 获取股票数据
# symbol = "600519.SS"
symbol = "603305.SS"
start_date = "2025-03-01"
end_date = "2025-03-10"

data = yf.download(symbol, start=start_date, end=end_date)
print(data.head())
