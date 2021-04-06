"""
分别定义实现加减乘除的函数
"""

def add(a,*b):     #一个*号参数收集，*b返回的是一个元组，a为明确参数，必须写
    result=a
    for i in b:
        result+=i
    return result

def reduce(a,b):
    return a-b

def ride(a,b):
    return a*b

def except1(a,b):
    return a/b

def fun(a,*b):     #一个*号参数收集，*b返回的是一个元组，a为明确参数，必须写
    print('a=',a)
    print('b=',b)

def bar(a,**b):   #两个*号参数收集，**b返回的是一个字典，必须以赋值的形式传入参数，a为明确参数，必须写
    print('a=',a)
    print('b=',b)

print(add(2,1,5,5,6,4,8,65))
print(reduce(2,1))
print(ride(2,1))
print(except1(2,1))
print(fun(1))
print(bar(1))
print(bar(1,c=2,d=3,e=4,f=5))  #**b必须以赋值的形式传参，返回的是一个字典
