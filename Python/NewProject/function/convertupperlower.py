'''
定义一个函数，大写转小写，小写转大写
'''

def convert(s):    #转换的意思
    lst=[i.upper() if i==i.lower() else i.lower() for i in s] #列表解析
    s_str=''.join(lst)
    return s_str

print(convert('Abc'))
