'''
现有字符串"Life is short You need python"，统计当中每个字符出现的次数
'''

s='Life is short You need python'
d={}

for letter in s:
    if letter.isalpha():
        if letter in d:
            d[letter]+=1
        else:
            d[letter]=1

print(d)
