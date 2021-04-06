'''
特殊函数
(lambda x,y,z,...：do something):只用一行定义函数的函数
(map(func,*iterables)):使用函数func迭代后面iterator里的每一个元素，可以是多个iterator
(reduce(func,iterable))：reduce中的func函数必须有两个参数，先将后面iterable中的第1、2个元素进行操作，将得到的结果与第三个元素操作，最后得到一个结果
(filter(func or None,iterable)):参数func相当于一个限制条件（过滤条件），将iterable中的元素进行过滤
(zip(*iterable)):并行迭代,抛弃多余项，自动匹配
'''

import functools

lam=lambda x:x+3
print(lam(3))

numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(lam,numbers)))
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[3,4,5,6,7]
s=[x+y+z for x,y,z in zip(lst1,lst2,lst3)]    #列表解析方法实现相加
print(s)
s2=list(map(lambda x,y,z:x+y+z,lst1,lst2,lst3))     #map方法实现相加
print(s2)

print(functools.reduce(lambda x,y:x+y,numbers))
print(functools.reduce(lambda x,y:x*y,numbers))

print(list(filter(lambda x:x>5,lst3)))    #使用filter函数
print([i for i in lst3 if i>5])           #列表解析方法

