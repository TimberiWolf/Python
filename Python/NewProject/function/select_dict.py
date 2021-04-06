'''
假设有数据：d={'a':39,'b':40,'c':99,'d':100}（字典的键值对还可以增加）
编写函数，实现对这个字典中键值对的查询，例如向函数提供参数a=1,b=40等参数，
查询这些是否为此数据的值
'''

def select(dct,**key_value):
    r = {k:v for k,v in key_value.items() if dct.get(k)==v} #字典解析，用法同列表解析
    return r

d={'a':39,'b':40,'c':99,'d':100}
fr=select(d,a=3,b=10,c=99,d=20)
print(fr)