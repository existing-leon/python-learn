import datetime

import yfinance as yf

from datetime import date

# 获取旭升集团股票数据
symbol = "603305.SS"
start_date = "2022-01-01"
end_date = date.today()

# 获取当前日期
current_date = date.today()

data = yf.download(symbol, start=start_date, end=end_date)
print(data.head())
