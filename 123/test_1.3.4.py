from PIL import Image
from pylab import *
import imtools

# 直方图均衡化
im = array(Image.open('../image/AquaTermi_lowcontrast.JPG').convert('L'))
im2, cdf = imtools.histeq(im)

figure()
gray()
subplot(221)
axis('off')
title(r'before')
imshow(im)

subplot(222)
axis('off')
title(r'after')
imshow(im2)

subplot(223)
hist(im.flatten(), 128)

subplot(224)
hist(im2.flatten(), 128)

show()