# 作者：Tom
# 开发时间：2022/9/28 9:17
from PIL import Image
import numpy as np
from numpy import *

im = array(Image.open('../image/empire.jpg'))
print(im.shape, im.dtype)
im = array(Image.open('../image/empire.jpg').convert('L'), 'f')  # (f 是将数据转为浮点型)
print(im.shape, im.dtype)
