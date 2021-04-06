'''
条件语句
输入一个数，将该数与10比较，等于10时，输出一句奖励的话
'''

number=input('Your number:')

if number.isdigit():
    if int(number) == 10:
        print('You are smart!')
    elif int(number) > 10:
        print('Your number is more than 10')
    else:
        print('Your number is less than 10')
else:
    print('Please input number!')