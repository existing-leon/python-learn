import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

"""
1）低方差过滤法
对于特征的选择，可以直接基于方差来判断，这是最简单的。低方差的特征意味着该特征的所有样本值几乎相同，对预测影响极小，可以将其去掉。
"""
# numpy 数组
X_np = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# pandas DataFrame
X_df = pd.DataFrame({
    'feat1': [1, 5, 9],
    'feat2': [2, 6, 10],
    'feat3': [3, 7, 11],
    'feat4': [4, 8, 12]
})
# 低方差过滤：删除方差低于 0.01 的特征
var_thresh = VarianceThreshold(threshold=0.01)
"""
        X : array-like of shape (n_samples, n_features)
            Input samples.
"""
X_np_filtered = var_thresh.fit_transform(X_np)
print(X_np_filtered)
X_df_filtered = var_thresh.fit_transform(X_df)
print(X_df_filtered)
print()

"""
2）相关系数法
通过计算特征与目标变量或特征之间的相关性，筛选出高相关性特征（与目标相关）或剔除冗余特征（特征间高度相关）。


（1）皮尔逊相关系数
皮尔逊相关系数（Pearson Correlation）用于衡量两个变量的线性相关性，取值范围[-1,1]。

	正相关：值接近1，说明特征随目标变量增加而增加。
	负相关：值接近-1，说明特征随目标变量增加而减少。
	无关：值接近0，说明特征和目标变量无明显关系。

现有一数据集包括不同渠道广告投放金额与销售额。

"""
# 使用pandas.DataFrame.corrwith(method="pearson")计算各个特征与标签间的皮尔逊相关系数。
advertising = pd.read_csv("data/advertising.csv")
advertising.drop(advertising.columns[0], axis=1, inplace=True)
advertising.dropna(inplace=True)
X = advertising.drop("Sales", axis=1)
y = advertising["Sales"]
# 计算皮尔逊相关系数
print(X.corrwith(y, method="pearson"))
print()

# 使用pandas.DataFrame.corr(method="pearson")计算皮尔逊相关系数矩阵。
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 计算皮尔逊相关系数矩阵
corr_matrix = advertising.corr(method='pearson')
# 可视化热图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Featurn Correlation Matrix')
plt.show()

"""
（2）斯皮尔曼相关系数
斯皮尔曼相关系数（Spearman’s Rank Correlation Coefficient）的定义是等级变量之间的皮尔逊相关系数。
用于衡量两个变量之间的单调关系，即当一个变量增加时，另一个变量是否总是增加或减少（不要求是线性关系）。
适用于非线性关系或数据不符合正态分布的情况。

斯皮尔曼相关系数的取值范围为[-1,1]：  

ρ=1：完全正相关（一个变量增加，另一个变量也总是增加）。
ρ=-1：完全负相关（一个变量增加，另一个变量总是减少）。
ρ=0：无相关性。

"""
import pandas as pd

# 每周学习时长
X = [[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]
# 数学考试成绩
y = [55, 65, 70, 75, 85, 50, 60, 72, 80, 58]
# 计算斯皮尔曼相关系数
X = pd.DataFrame(X)
y = pd.Series(y)

print(X.corrwith(y, method='spearman'))
print()

"""
3）主成分分析（PCA）
主成分分析（Principal Component Analysis，PCA）是一种常用的降维技术，通过线性变换将高维数据投影到低维空间，同时保留数据的主要变化模式。
使用sklearn.decomposition.PCA进行主成分分析。参数n_components若为小数则表示保留多少比例的信息，为整数则表示保留多少个维度。
"""
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

n_samples = 1000
# 第1个主成分方向
component1 = np.random.normal(0, 1, n_samples)
# 第2个主成分方向
component2 = np.random.normal(0, 0.2, n_samples)
# 第3个方向（噪声，方差较小）
noise = np.random.normal(0, 0.1, n_samples)
# 构造3维数据
X = np.vstack([component1 - component2, component1 + component2, component2 + noise]).T

# 标准化
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# 应用PCA，将3维数据降维到2维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_standardized)

# 可视化
# 转换前的3维数据可视化
fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(121, projection="3d")
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c="g")
ax1.set_title("Before PCA (3D)")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")
# 转换后的2维数据可视化
ax2 = fig.add_subplot(122)
ax2.scatter(X_pca[:, 0], X_pca[:, 1], c="g")
ax2.set_title("After PCA (2D)")
ax2.set_xlabel("Principal Component 1")
ax2.set_ylabel("Principal Component 2")
plt.show()
