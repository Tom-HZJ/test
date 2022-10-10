# 作者：Tom
# 开发时间：2022/9/28 8:59
from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('../image/empire.jpg').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息,将真彩色图像转换为灰度图像
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')  # 关闭第一个图的坐标系

# 新建一个图像
figure()
# 绘制灰度图像直方图
hist(im.flatten(), 128, color='black')
show()
