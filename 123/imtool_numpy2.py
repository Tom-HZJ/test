# 作者：Tom
# 开发时间：2022/9/28 9:24

from pylab import *
from matplotlib.pyplot import figure, gray
from PIL import Image
from numpy import *

im1 = array(Image.open('../image/empire.jpg').convert('L'))
# pil_im = Image.fromarray(im1)
# pil_im.show()
print(int(im1.min()), int(im1.max()))
im2 = 255 - im1
print(int(im2.min()), int(im2.max()))
im3 = (100.0 / 255) * im1 + 100
print(int(im3.min()), int(im3.max()))
im4 = 255.0 * (im1 / 255.0) ** 2
print(int(im4.min()), int(im4.max()))

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))  # 设定n*n排列方式，这里设置的是2*2，nrows行，ncols列，figsize设定窗口大小

axis('equal')
gray()

axes[0, 0].imshow(im1)
axes[0, 0].set_title("im")

axes[0, 1].imshow(im2)
axes[0, 1].set_title("im2")

axes[1, 0].imshow(im3)
axes[1, 0].set_title("im3")

axes[1, 1].imshow(im4)
axes[1, 1].set_title("im4")

show()
