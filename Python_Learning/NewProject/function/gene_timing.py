'''
通用时间计算装饰器
'''
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)  #装饰的函数可以传参数或不传参数,不限形式的参数
        stop=time.time()
        print(func.__name__,stop-start)
    return wrapper

@timethis
def countdown(n):
    while n>0:
        n-=1

@timethis
def test_list_append():
    lst=[]
    for i in range(100000000):
        lst.append(i)

@timethis
def test_list_compre():
    [i for i in range(100000000)]

countdown(1000000)
countdown(100000000)

test_list_append()
test_list_compre()