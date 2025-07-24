""""""
"""
Python基本的日期与时间功能都在标准库的datetime模块中
"""
from datetime import datetime

date1 = datetime(year=2000, month=1, day=1)
date2 = datetime.now()
print(date1)
print(date2)
print(date1.year)
print(date1.month)
print(date1.day)
print(date2.weekday())
print(date2.strftime('%A'))
print(date2 - date1)
print()

"""
pandas的日期时间类型默认是datetime64[ns]。
	针对时间戳数据，pandas提供了Timestamp类型。它本质上是Python原生datetime类型的替代品，但是在性能更好的numpy.datetime64类型的基础上创建。对应的索引数据结构是DatetimeIndex。
	针对时间周期数据，pandas提供了Period类型。这是利用numpy.datetime64类型将固定频率的时间间隔进行编码。对应的索引数据结构是PeriodIndex。
	针对时间增量或持续时间，pandas提供了Timedelta类型。Timedelta是一种代替Python原生datetime.timedelta类型的高性能数据结构，同样是基于numpy.timedelta64类型。对应的索引数据结构是TimedeltaIndex。
"""
## 1）datetime64：
# o_datetime()可以解析许多日期与时间格式。对to_datetime()传递一个日期会返回一个Timestamp类型，传递一个时间序列会返回一个DatetimeIndex类型。
import pandas as pd

print(pd.to_datetime('2015-01-01'))
print(pd.to_datetime(["4th of July, 2015", "2015-Jul-6", "07-07-2015", "20150708"], format="mixed"))
print()

# 在加载数据时, 可以通过 to_datetime() 将数据中的列解析为 datetime64
df = pd.read_csv('data/weather.csv')
print(df['date'].tail())
print()
print(pd.to_datetime(df['date'].tail()))
print()

# 在加载数据时, 也可以通过 parse_dates 参数将指定列解析为 datetime64
df = pd.read_csv('data/weather.csv', parse_dates=[0])
print(df['date'].tail())
print()

## 2）提取日期的各个部分
# 提取 Timestamp
d = pd.Timestamp('2015-01-01 09:08:07.123456')
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print()

# 对于 Series 对象, 需要使用 dt 访问器
df = pd.read_csv('data/weather.csv', parse_dates=[0])
df_date = pd.to_datetime(df['date'])
df['year'] = df_date.dt.year
df['month'] = df_date.dt.month
df['day'] = df_date.dt.day
print(df[['date', 'year', 'month', 'day']].tail())
print()

## 3）period
# 可以通过 to_period() 方法和一个频率代码将 datetime64 类型转换为 period 类型
df = pd.read_csv('data/weather.csv')
df['quarter'] = pd.to_datetime(df['date']).dt.to_period('Q')
print(df[['date', 'quarter']].head())
print()

## 4）timedelta64
# 当用一个日期减去另一个日期, 返回的结果是 timedelta64 类型
df = pd.read_csv('data/weather.csv', parse_dates=[0])
df_date = pd.to_datetime(df['date'])
timedelta = df_date - df_date[0]
print(timedelta.head())
print()

"""
使用时间作为索引
"""
# 将datetime64类型的数据设置为索引，得到的就是DatetimeIndex。
df = pd.read_csv("data/weather.csv")
df["date"] = pd.to_datetime(df["date"])  # 将date列转换为datetime64类型
df.set_index("date", inplace=True)  # 将date列设置为索引
df.info()
print()

# 将时间作为索引后可以直接使用时间进行切片取值。
print(df.loc["2013-01":"2013-06"])  # 获取2013年1~6月的数据
print()
print(df.loc['2015'])
print()

# 可以通过between_time()和at_time()获取某些时刻的数据
print(df.between_time("9:00", "11:00"))  # 获取9:00到11:00之间的数据
print()
print(df.at_time("3:33"))  # 获取3:33的数据
print()

# 将timedelta64类型的数据设置为索引，得到的就是TimedeltaIndex。
df = pd.read_csv("data/weather.csv", parse_dates=[0])
df_date = pd.to_datetime(df["date"])
df["timedelta"] = df_date - df_date[0]  # 得到timedelta64类型的数据
df.set_index("timedelta", inplace=True)  # 将timedelta列设置为索引
df.info()
print()

# 将时间作为索引后可以直接使用时间进行切片取值。
print(df.loc["0 days":"5 days"])
print()

"""
生成时间序列：

date_range():
    date_range() 通过开始日期、结束日期和频率代码（可选）创建一个有规律的日期序列, 默认的频率是天
"""
print(pd.date_range('2015-07-03', '2015-07-10'))
print()

# 日期范围不一定非是开始时间与结束时间, 也可以是开始时间与周期数 periods
print(pd.date_range('2015-07-03', periods=5))
print()

# 可以通过 freq 参数设置时间频率, 默认值是 D, 此处改为 h, 按小时变化的时间戳
print(pd.date_range('2015-07-03', periods=5, freq='h'))
print()

"""
2）时间频率与偏移量
（1）可通过freq参数设置时间频率
下表为常见时间频率代码与说明：

D	        天（calendar day，按日历算，含双休日）
B	        天（business day，仅含工作日）
W	        周（weekly）
ME / M	    月末（month end）
BME	        月末（business month end，仅含工作日）
MS	        月初（month start）
BMS	        月初（business month start，仅含工作日）
QE / Q	    季末（quarter end）
BQE	        季末（business quarter end，仅含工作日）
QS	        季初（quarter start）
BQS	        季初（business quarter start，仅含工作日）
YE / Y	    年末（year end）
BYE	        年末（business year end，仅含工作日）
YS	        年初（year start）
BYS	        年初（business year start，仅含工作日）
h	        小时（hours）
bh	        小时（business hours，工作时间）
min	        分钟（minutes）
s	        秒（seconds）
ms	        毫秒（milliseonds）
us	        微秒（microseconds）
ns	        纳秒（nanoseconds）

（2）偏移量
可以在频率代码后面加三位月份缩写字母来改变季、年频率的开始时间。
	QE-JAN、BQE-FEB、QS-MAR、BQS-APR等
	YE-JAN、BYE-FEB、YS-MAR、BYS-APR等

"""
print(pd.date_range("2015-07-03", periods=10, freq="QE-JAN"))  # 设置1月为季度末
print()

"""
同理，也可以在后面加三位星期缩写字母来改变一周的开始时间。
	W-SUN、W-MON、W-TUE、W-WED等
"""
print(pd.date_range("2015-07-03", periods=10, freq="W-WED"))  # 设置周三为一周的第一天
print()

"""
在这些代码的基础上，还可以将频率组合起来创建的新的周期。例如，可以用小时（h）和分钟（min）的组合来实现2小时30分钟。
"""
print(pd.date_range("2015-07-03", periods=10, freq="2h30min"))
print()

"""
重新采样：
理时间序列数据时，经常需要按照新的频率（更高频率、更低频率）对数据进行重新采样。
可以通过resample()方法解决这个问题。resample()方法以数据累计为基础，
会将数据按指定的时间周期进行分组，之后可以对其使用聚合函数。
"""
df = pd.read_csv("data/weather.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
print(df[["temp_max", "temp_min"]].resample("YE").mean())  # 将数据按年分组,并计算每年的平均最高最低温度
