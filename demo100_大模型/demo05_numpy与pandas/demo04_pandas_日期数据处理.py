""""""
"""
to_datetime() 进行日期格式转换
参数说明：
arg	        要转换为日期时间的对象
errors	    ignore,raise,coerce, 默认为ignore,表示无效的解析将会返回原值
dayfirst	指定日期解析顺序。如果为True，则以日期开头解析日期，例如：“10/11/12”解析为2012-11-10。默认false
yearfirst	如果为True，则以日期开头解析，例如：“10/11/12”解析为2010-11-12。如果dayfirst和yearfirst都为True，则yearfirst在前面。默认false。当日期字符串格式不明确时，指定年份是否在最前面。当日期字符串是 '2010/1/4' 这种形式，由于年份是 4 位数字，pandas 能很清晰地识别出这是年份，所以即使 yearfirst 为 False，也不会影响其正确解析
utc	        返回utc，即协调世界时间
format	    格式化显示时间的格式，字符串，默认值为None
exact	    要求格式完全匹配
unit	    参数的单位表示时间的单位
infer_datetime_format	如果为True且未给出格式，则尝试基于第一个非nan元素推断datetime字符串的格式，如果可以推断，则切换到更快的解析方法。在某些情况下，这可以将解析速度提高5-10倍。
origin	    默认值为unix,定义参考日期1970-01-01
cache	    使用唯一的已转换日期缓存来应用日期时间转换。在解析重复日期字符串时产生显著的加速。
"""

import pandas as pd

# 将字符串字段转换为日期类型
df = pd.DataFrame(
    {
        'gmv': [100, 200, 300, 400],
        'trade_date': ['2025-01-06', '2023-10-31', '2023-12-31', '2023-01-05']
    }
)
df['ymd'] = pd.to_datetime(df['trade_date'])
print(df)
print()

# 获取年月日
df['yy'], df['mm'], df['dd'] = df['ymd'].dt.year, df['ymd'].dt.month, df['ymd'].dt.day
print(df)
print()

# 获取星期
df['week'] = df['ymd'].dt.day_name()
print(df)
print()

# 获取日期所在季度
df['quarter'] = df['ymd'].dt.quarter
print(df)
print()

# 判断日期是否月底年底
df['mend'] = df['ymd'].dt.is_month_end
df['yend'] = df['ymd'].dt.is_year_end
print(df)
print()

"""
to_period() 获取统计周期
freq：这是 to_period() 方法最重要的参数，用于指定要转换的时间周期频率
常见的取值如下：
	"D"：按天周期，例如 2024-01-01 会转换为 2024-01-01 这个天的周期。
	"W"：按周周期，通常以周日作为一周的结束，比如日期落在某一周内，就会转换为该周的周期表示。
	"M"：按月周期，像 2024-05-15 会转换为 2024-05。
	"Q"：按季度周期，一年分为四个季度，日期会转换到对应的季度周期，例如 2024Q2 。
	"A" 或 "Y"：按年周期，如 2024-07-20 会转换为 2024 。
"""
df['ystat'] = df['ymd'].dt.to_period('Y')
df['mstat'] = df['ymd'].dt.to_period('M')
df['qstat'] = df['ymd'].dt.to_period('Q')
df['wstat'] = df['ymd'].dt.to_period('W')
print(df)
