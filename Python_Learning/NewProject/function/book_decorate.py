'''
装饰器
'''

def p_deco(func):
    def wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return wrapper

@p_deco
def book(name):
    return 'the name of my book is {0}'.format(name)
