# 作者：Tom
# 开发时间：2022/9/28 9:15
from PIL import Image
from pylab import *

im = array(Image.open('../image/empire.jpg'))
imshow(im)
print('Please click 3 points')
x = ginput(3)
print('you clicked:', x)
show()
