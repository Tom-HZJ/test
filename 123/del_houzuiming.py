# 作者：Tom
# 开发时间：2022/9/25 13:11
import os
from os import listdir

path = '../image/'

for file_name in listdir(path):
    if file_name.endswith('.png'):
        os.remove(path + file_name)

print("File remove successfully")
