'''
对比for循环和列表解析运行速度
'''

import time

def foo(func):
    def bar():
        start=time.time()
        func()
        stop=time.time()
        return stop-start
    return bar

@foo
def test_list_append():
    lst=[]
    for i in range(100000000):
        lst.append(i)

@foo
def test_list_compre():
    [i for i in range(100000000)]

a=test_list_append()
b=test_list_compre()

print('test list append time:',a)
print('test list comprehension time:',b)
print('append/compre:',round(a/b,3))