'''
创建一个数据集，里面为1~10的随机整数，共计100个，并计算每个数字出现的字数
'''

import random

lst=[]

for i in range(1,101):
    n=random.randint(1,10)
    lst.append(n)

print('数据集：',lst)

d={}
for n in lst:
    if n in d:
        d[n]+=1
    else:
        d[n]=1

print(d)

# for i in range(1,11):
#     print('数字{}出现的次数为:'.format(i),lst.count(i))