# 作者：Tom
# 开发时间：2022/9/28 11:08
from PIL import Image
from numpy import *
import os


# 工具包
def get_imlist(path):
    """ 返回目录中所有JPG图像的文件名列表 """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """ 使用PIL对象重新定义图像数组的大小 """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    """ 对一幅灰度图像进行直方图均衡化 """
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins)
    cdf = imhist.cumsum()  # 累积分布函数
    cdf = 255 * cdf / cdf[-1]  # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(imlist, imname=None):
    """ 计算图像列表的平均图像 """
    # 打开第一幅图像，将其存储在浮点型数组中
    average = array(Image.open(imlist[0]), 'f')
    for imnae in imlist[1:]:
        try:
            average += array(Image.open(imname))
        except:
            print(imname + '...skipped')
        averageim /= len(imlist)
    # 返回uint8类型的平均图像
    return array(averageim, 'uint8')