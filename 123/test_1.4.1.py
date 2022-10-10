# 作者：Tom
# 开发时间：2022/9/28 20:18
from PIL import Image
from pylab import *
from scipy.ndimage import filters, gaussian_filter

im1 = array(Image.open('../image/empire.jpg').convert('L'))
# 弃用警告：请使用 `scipy.ndimage` 命名空间中的 `gaussian_filter`，`scipy.ndimage.filters` 命名空间已弃用。
im2 = gaussian_filter(im1, 0)
im3 = gaussian_filter(im1, 2)
im4 = gaussian_filter(im1, 5)
im5 = gaussian_filter(im1, 10)

fig, axes = plt.subplots(ncols=4, figsize=(15, 5))
# axis('equal')
gray()

axes[0].imshow(im2)
axes[0].set_title("0")

axes[1].imshow(im3)
axes[1].set_title("2")

axes[2].imshow(im4)
axes[2].set_title("5")

axes[3].imshow(im5)
axes[3].set_title("10")
# axes[1, 1].set_title("10")

show()
