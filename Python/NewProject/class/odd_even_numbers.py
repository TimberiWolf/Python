'''
创建一个类，当这个类实例化的时候，自动将数据集中的偶数和奇数分别用两个属性引用
'''

class Nmbers:
    odd = []
    even = []
    def __init__(self):
        pass

    @classmethod
    def input_numbers(cls,*args):
        for i in args:
            if i%2==0:
                cls.even.append(i)
            else:
                cls.odd.append(i) 

a= Nmbers.input_numbers(1,2,3,4,5,6,7,8,9)
print(Nmbers.odd)
print(Nmbers.even)