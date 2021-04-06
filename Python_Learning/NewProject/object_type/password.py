'''
编写程序，利用“凯撒密码”方案，对用户输入的文字加密操作。
'''

letter=input('Please input the key:')
n=3 #偏移量
pwd=ord(letter)+n
pwd_letter=chr(pwd)
print(letter,'==>',pwd_letter)
