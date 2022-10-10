# 作者：Tom
# 开发时间：2022/9/28 12:02
# -*- coding: utf-8 -*-

import os
import pickle

from PIL import Image
from pylab import *
from numpy import *
import pca

# 相对路径
path = '../fontimages/a_thumbs/'
# 利用pca.py中的get_imlist()这个在前文中有提到
imlist = pca.get_imlist(path)
# 打开一副图像，获取其大小
im = array(Image.open(imlist[0]))
# 获取图像的大小
m, n = im.shape[0:2]
# 获取图像的数目
imnbr = int(len(imlist))
# 创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten()
                  for im in imlist], 'f')
# 执行PCA操作
V, S, immean = pca.pca(immatrix)
# 显示一些图像（均值图像和前7个模式）
figure()
gray()
subplot(2, 4, 1)
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i + 2)
    imshow(V[i].reshape(m, n))

show()

# # 保存均值和主成分数据
# f = open('font_pca_modes.pkl', 'wb')
# pickle.dump(immean,f)
# pickle.dump(V,f)
# f.close()
#
#
# # 载入均值和主成分数据
# f = open('font_pca_modes.pkl', 'rb')
# immean = pickle.load(f)
# V = pickle.load(f)
# f.close()
#
# # 打开文件并保存
# with open('font_pca_modes.pkl', 'wb') as f:
#   pickle.dump(immean,f)
#   pickle.dump(V,f)

# 打开文件并载入
with open('font_pca_modes.pkl', 'rb') as f:
  immean = pickle.load(f)
  V = pickle.load(f)