'''
条件语句
编写程序，随机生成一个10以内的整数，如果该整数大于圆周率Π，就将其当作直径计算圆的周长和面积，否则就当作半径计算
'''

import math,random

a=random.randint(1,10)

if a > math.pi:
    perimeter=a*math.pi
    area=math.pi*pow(a/2,2)
    print('随机数为：',a)
    print('周长为{0}，面积为{1}'.format(round(perimeter,2),round(area,2)))
else:
    perimeter=2*a*math.pi
    area=math.pi*pow(a,2)
    print('随机数为：',a)
    print('周长为{0}，面积为{1}'.format(round(perimeter,2),round(area,2)))