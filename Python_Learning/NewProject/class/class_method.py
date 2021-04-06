'''
类方法 & 静态方法
'''

class Foo:
    @classmethod
    def foo(cls,x):
        return x*2
    @staticmethod
    def bar():
        print('This a static method')

print(Foo.foo(3))
Foo.bar()