'''
编写程序，实现大小写字母转换
'''

# letter=input('Please input:')
# after_letter=letter
# if letter.islower():
#     after_letter=letter.upper()
# else:
#     after_letter=letter.lower()
#
# print(letter,'==>',after_letter)


'''
字符串大小写转换
'''

word=input('Please input:')
word_list=[]

for i in word:
    if i.islower():
        word_list.append(i.upper())
    else:
        word_list.append(i.lower())

new_word=''.join(word_list)
print(word,'==>',new_word)

