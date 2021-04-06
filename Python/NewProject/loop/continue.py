'''
打印出10以内的偶数
'''

a=0
even_numbers=[]
while a<10:
    a += 1
    if a%2!=0:
        continue
    else:
        even_numbers.append(a)
print(even_numbers)
