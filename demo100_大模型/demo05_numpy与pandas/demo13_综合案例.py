""""""
"""
1 业务背景
在房地产市场中，准确的房价预测和深入的市场分析对于房产开发商、投资者以及购房者都至关重要。房产开发商需要根据市场趋势和不同因素对房价的影响来制定合理的定价策略，优化项目规划；投资者需要评估房产的潜在价值和投资回报率，做出明智的投资决策；购房者则希望了解市场行情，找到性价比高的房产。
某大型房地产数据研究机构收集了大量不同地区的房屋销售数据，这些数据包含了房屋的各种属性信息以及销售相关信息。为了更好地服务于市场参与者，该机构计划对这些数据进行全面深入的分析，挖掘数据背后的规律和价值。具体目标包括：
	探究不同房屋特征（如卧室数量、浴室数量、居住面积等）对房价的影响程度，以便为房价预测模型提供依据。
	分析不同地区（以邮政编码划分）的房地产市场差异，了解各地区的房价水平、市场活跃度等情况。
	研究房屋的建造年份、翻新年份等时间因素对房价的影响，以及不同时间段的市场趋势变化。
	通过可视化手段直观展示数据的分布和关系，为决策提供清晰的参考。

2 数据源介绍
字段名	    含义	                        数据类型	            说明
id	            房屋销售记录的唯一标识符	整数	                用于唯一标识每一条房屋销售记录
date	        房屋销售日期	            日期时间类型	        记录房屋实际完成销售的日期，可用于时间序列分析，观察不同时间段的市场趋势
price	        房屋销售价格	            数值型	            反映房屋在销售时的成交金额，是分析的核心指标之一，受多种房屋特征和市场因素影响
bedrooms	    卧室数量	                整数	                体现房屋的居住功能布局，卧室数量的多少会影响房屋的整体实用性和市场需求
bathrooms	    浴室数量	                整数	                同样是影响房屋舒适度和实用性的重要因素，与卧室数量共同影响房屋的居住体验
sqft_living	    居住面积（平方英尺）	    数值型	            指房屋内部可供居住使用的实际面积，是影响房价的关键因素之一
sqft_lot	    土地面积（平方米）	        数值型	            包括房屋所在土地的总面积，土地面积大小会影响房屋的整体价值和使用空间
floors	        楼层数	                整数	                房屋的楼层数量会影响房屋的视野、采光、私密性等方面，进而对房价产生影响
waterfront	    是否临水	                整数（0 或 1）	    0 表示房屋不临水，1 表示房屋临水，临水房屋通常具有更高的景观价值和市场价格
view	        景观评分	                整数（0 - 4）	    对房屋周边景观的评分，评分越高表示景观越好，景观质量会影响房屋的吸引力和价格
condition	    房屋状况评分	            整数（1 - 5）	    反映房屋的整体状况，包括房屋的结构、装修、设施等方面的维护情况
grade	        房屋整体质量评分	        整数（1 - 13）	    综合评估房屋的建筑质量、设计水平等因素，是衡量房屋价值的重要指标
sqft_above	    地上面积（平方米）	        数值型	            指房屋地面以上部分的建筑面积，不包括地下室面积
sqft_basement	地下室面积（平方米）	    数值型	            地下室面积可作为额外的存储空间或功能区域，对房屋的实用性和价值有一定影响
yr_built	    建造年份	                整数	                记录房屋的建成时间，房屋的建造年份会影响房屋的折旧程度、建筑风格和市场竞争力
yr_renovated	翻新年份	                整数              	0 表示房屋未进行过翻新，非 0 值表示房屋进行翻新的具体年份，翻新可以提升房屋的价值和居住体验
zipcode	        邮政编码	                整数	                用于标识房屋所在的地理位置区域，不同的邮政编码区域可能具有不同的市场特征和房价水平
lat	            纬度	                    数值型	            房屋所在位置的纬度坐标，结合经度可确定房屋的具体地理位置
long	        经度	                    数值型	            房屋所在位置的经度坐标，与纬度共同用于地理空间分析

3.1 数值型列的描述性统计指标
	均值（Mean）：一组数据的平均值，反映数据的集中趋势。例如，房价的均值可以让我们了解该地区房屋的平均销售价格水平。
	中位数（Median）：将数据按升序或降序排列后，位于中间位置的数值。当数据存在极端值时，中位数比均值更能代表数据的一般水平。
	标准差（Standard Deviation）：衡量数据相对于均值的离散程度。标准差越大，说明数据越分散；反之，则越集中。比如房价的标准差可以反映该地区房价的波动情况。
	最小值（Minimum）：数据集中的最小数值，可用于了解数据的下限。
	最大值（Maximum）：数据集中的最大数值，可用于了解数据的上限。
	四分位数（Quartiles）：包括第一四分位数（Q1，25% 分位数）、第二四分位数（Q2，即中位数，50% 分位数）和第三四分位数（Q3，75% 分位数），能帮助了解数据的分布情况。

3.2 不同特征与房价的相关性
	使用皮尔逊相关系数衡量特征与房价之间的线性关系强度和方向，系数绝对值越接近 1，相关性越强；正系数表示正相关，负系数表示负相关。

3.3 按邮政编码、是否翻新、房龄分组的统计指标
	平均房价：各邮政编码区域内房屋的平均销售价格，用于对比不同区域的房价水平。
	平均居住面积：各区域内房屋居住面积的平均值，反映区域房屋规模情况。
	平均卧室数量：各区域内房屋卧室数量的平均值，体现区域房屋居住功能布局。

3.4 时间序列分析指标
	每年平均房价（Average Price per Year）：按销售年份分组计算的房屋平均销售价格，可用于观察房价随时间的变化趋势。

"""
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use('TkAgg')  # 或 'Qt5Agg', 'Agg'（Agg 无窗口，用于保存图像）
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体

# step1：数据读取
# 读取 CSV 文件
data = pd.read_csv('data/house_sales.csv')
data.info()
print()

# step2：数据清洗
# 检查缺失值
missing_values = data.isnull().sum()
print('各列缺失值数量：===> \n', missing_values, '\n')
# 处理缺失值, 这里简单地删除包含缺失值的行
data = data.dropna()
# 检查异常值, 以房价为例, 使用IQR方法
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data = data[(data['price'] >= lower_bound) & (data['price'] <= upper_bound)]
print(data, '\n')

# step3：数据类型转换
# 将日期列转换为日期类型
data['date'] = pd.to_datetime(data['date'])

# step4：创建新的特征
# 计算房屋的使用年限
data['age'] = data['date'].dt.year - data['yr_built']
# 创建新特征, 是否翻新
data['is_renovated'] = data['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)

# step5：数据探索性分析-描述性统计
# 选择数值型列
numeric_columns = data.select_dtypes(include=[np.number]).columns
# 计算描述性统计信息
description = data[numeric_columns].describe(percentiles=[0.25, 0.5, 0.75])
print('数值型列的描述性统计 ==> \n', description, '\n')

# step6：计算不同特征与房价的相关性
correlation = data[numeric_columns].corr()
print('各特征与房价的相关性 ==> \n', correlation['price'], '\n')

# step7：按邮政编码分组, 计算每组的平均房价、平均居住面积、平均卧室数量
zipcode_stats = data.groupby('zipcode').agg({
    'price': 'mean',
    'sqft_living': 'mean',
    'bedrooms': 'mean'
})
zipcode_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('不同邮政编码区域的统计信息 ==> \n', zipcode_stats, '\n')

# step8：按是否翻新分组，计算每组的平均房价、平均居住面积、平均卧室数量
renovation_stats = data.groupby('is_renovated').agg({
    'price': 'mean',
    'sqft_living': 'mean',
    'bedrooms': 'mean'
})
renovation_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('是否翻新分组的统计信息 ==> \n', renovation_stats, '\n')

# step9：按房屋使用年限分组（简单分为 5 个区间）
data['age_group'] = pd.cut(data['age'], bins=5)
age_stats = data.groupby('age_group').agg({
    'price': 'mean',
    'sqft_living': 'mean',
    'bedrooms': 'mean'
})
print('按房屋使用年限分组的统计信息 ==> \n', age_stats, '\n')

# step10：按年份分组，计算每年的平均房价
yearly_avg_price = data.groupby(data['date'].dt.year)['price'].mean()
print('每年的平均房价 ==> \n', yearly_avg_price, '\n')

# step11：按年份和是否翻新分组，计算每年不同翻新情况的平均房价
yearly_renovation_avg_price = data.groupby([data['date'].dt.year, 'is_renovated'])['price'].mean()
print('每年不同翻新情况的平均房价 ==> \n', yearly_renovation_avg_price, '\n')

# step12：可视化展示
# 房价分布直方图
plt.figure(figsize=(10, 6))
plt.hist(data['price'], bins=30, edgecolor='k')
plt.title('房价分布直方图')
plt.xlabel('房价')
plt.ylabel('频数')
plt.show()

# 卧室数量与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['bedrooms'], data['price'])
plt.title('卧室数量与房价的关系')
plt.xlabel('卧室数量')
plt.ylabel('房价')
plt.show()

# 各特征与房价的相关性热力图
plt.figure(figsize=(12, 8))
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title('各特征与房价的相关性热力图')
plt.show()

# 不同邮政编码区域平均房价的柱状图
plt.figure(figsize=(12, 6))
plt.bar(zipcode_stats.index.astype(str), zipcode_stats['avg_price'])
plt.title('不同邮政编码区域的平均房价')
plt.xlabel('邮政编码')
plt.ylabel('平均房价')
plt.xticks(rotation=45)
plt.show()

# 每年平均房价的折线图
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_price.index, yearly_avg_price)
plt.title('每年平均房价趋势')
plt.xlabel('年份')
plt.ylabel('平均房价')
plt.show()

# 不同翻新情况的房价箱线图
plt.figure(figsize=(10, 6))
data.boxplot(column='price', by='is_renovated')
plt.title('不同翻新情况的房价箱线图')
plt.xlabel('是否翻新')
plt.xticks([1, 2], ['未翻新', '已翻新'])
plt.ylabel('房价')
plt.suptitle('')  # 去掉默认的标题
plt.show()

# 房屋使用年限与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['price'])
plt.title('房屋使用年限与房价的关系')
plt.xlabel('房屋使用年限')
plt.ylabel('房价')
plt.show()
