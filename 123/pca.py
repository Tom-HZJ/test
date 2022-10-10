# 作者：Tom
# 开发时间：2022/9/28 12:14


from PIL import Image
from numpy import *
import os


def get_imlist(path):
    """返回目录中所有JPG图像的名称列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


def pca(X):
    """ 主成分分析：
    输入：矩阵 X，其中该矩阵中存储训练数据，每一行为一条训练数据
    返回：投影矩阵（按照维度的重要性排序）、方差和均值 """
    # 获取维数
    num_data, dim = X.shape
    # 数据中心化
    mean_X = X.mean(axis=0)
    X = X - mean_X
    if dim > num_data:
        # PCA- 使用紧致技巧
        M = dot(X, X.T)  # 协方差矩阵
        e, EV = linalg.eigh(M)  # 特征值和特征向量
        tmp = dot(X.T, EV).T  # 这就是紧致技巧
        V = tmp[::-1]  # 由于最后的特征向量是我们所需要的，所以需要将其逆转
        S = sqrt(e)[::-1]  # 由于特征值是按照递增顺序排列的，所以需要将其逆转
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        # PCA- 使用 SVD 方法PCA（ Principal Component Analysis，主成分分析）是一个非常有用的降维技巧
        U, S, V = linalg.svd(X)
        V = V[:num_data]  # 仅仅返回前 nun_data 维的数据才合理
    # 返回投影矩阵、方差和均值
    return V, S, mean_X
