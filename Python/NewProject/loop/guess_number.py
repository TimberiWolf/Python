'''
随机生成一个100以内的正整数，用户通过输入数字猜测随机数，次数不限
'''

import random

num_random=random.randint(1,100)
guess=0

while 1:
    guess+=1
    num=input('Please input integer from 1 to 100:')
    if not num.isdigit():
        print('Please input integer!')
    elif int(num)<0 or int(num)>100:
            print('Please input integer in 1 to 100!')
    else:
        if int(num)==num_random:
            print('You are so smart,only {} is True!'.format(guess))
            break
        elif int(num)>num_random:
            print('Your integer is bigger!')
        else:
            print('Your integer is smaller!')
