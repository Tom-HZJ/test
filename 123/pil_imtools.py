# 作者：Tom
# 开发时间：2022/9/21 9:41

# import os
#

# from PIL import Image
#
# img = Image.open('../image/alcatraz1.jpg').convert('L')
# img.show()

# 转换图像格式
from PIL import Image
import os
import glob

path = '../image/'
filelist = glob.glob(os.path.join(path, '*'))

for inflie in filelist:
    outlife = os.path.splitext(inflie)[0] + '.png'
    if inflie != outlife:
        try:
            Image.open(inflie).save(outlife)
        except IOError:
            print("cannot covert", inflie)
