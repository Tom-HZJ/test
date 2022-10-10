# 作者：Tom
# 开发时间：2022/9/27 17:06

# plt.plot(x, y, fmt='xxx', linestyle（线的样式）=, marker（点的样式）=, color（点、线的颜色）=, linewidth（线的粗细）=, markersize（点的大小）=, label=, )  函数介绍
# axis('off')   #关闭坐标显示
# plot(x, y)  #默认为蓝色实线
# plot(x, y, 'r*')  # 红色星状标记
# plot(x, y, 'go-')  #带有圆圈标记的绿线
# plot(x, y, 'ks:')  #带有正方形标记的黑色虚线
from PIL import Image
from pylab import *

im = array(Image.open('../image/empire.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2], color='red')

title('Plotting: "empire.jpg"')

show()
