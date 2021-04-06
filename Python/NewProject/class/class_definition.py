'''
定义类的方式
'''

class SuperMan:     #class,定义类的关键词，后面紧跟着类的名称，首字母大写
    '''
    a class of superman      #类的文档
    '''

    def __init__(self,name):    #初始化方法，定义属性
        self.name=name
        self.gender=1   #1:male男性
        self.single=False
        self.illness=False

    def nine_negative_kungfu(self):    #普通方法
        return 'Ya! You have to die.'

guojing=SuperMan('guojing')      #实例化
print(guojing.name)
print(guojing.gender)
kongfu=guojing.nine_negative_kungfu()
print(kongfu)