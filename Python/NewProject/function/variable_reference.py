'''
变量引用
global,全局匹配,声明变量为全局变量
nonlocal,非本地匹配，可匹配到上一层，标识变量为上一级变量，只能用于嵌套函数
利用 global和 nonlocal可修改变量
'''

a=1
def foo():
    # global a
    # a=a+1
    b=a+1    #赋值引用只能在foo()中重新定义变量，不能直接使用全局变量a，要么使用global语句声明一下
    return b
print(foo())


def bar():
    b = 2
    def foobar():
        nonlocal b
        b=b+3
        return b
    foobar()
    return b

print(bar())

x=3   #全局变量x
def f():
    x=5    #重新声明的局部变量x，只作用于函数体内，与全局变量x无关联
    return x

print(f())