# 作者：Tom
# 开发时间：2022/9/23 9:15

#字典
score={'张三':100, '李四':20,'王五':30}
# print(score['张三'])
#
# print(score.get('李四'))
# print(score.get('太极'))
#
# print('张三' in score)  #查看张三在不在
# print('太极' not in score)#查看太极在不在
#
# del score['张三']    #删除字典中的某个
# print(score)
#
# score['晨晨']=98     #添加字典
# print(score)


keys =score.keys()
print(keys)
print(type(keys))
print(list(score))

values =score.values()
print(values)
print(type(values))
print(list(values))








# lst = [22, 2, 15, 222, 52]
# lst.sort()  #升序
# print(lst)
# lst.sort(reverse=True)    #降序
# print(lst)

# lst.remove('hello')
# lst.remove(20)
# lst.pop()
# lst[1:3] = []#赋予一个空列表，就可以进行切片操作了
#
# print(lst)

# print(lst.index('hello', -3, -1)

# del lst
# print(lst)
