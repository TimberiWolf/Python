'''
编写程序，根据输入的半径，计算圆的面积
'''
import math

r=input('请输入半径：')
'''
def isNum(s):
    for i in s:
        if i.isdigit():
            continue
        else:
            return False
    return True
'''
if r.isdigit():
    area = math.pow(float(r), 2) * math.pi
    print('圆的面积为{0}'.format(round(area, 2)))
else:
    print('Tip:please input numbers!')




