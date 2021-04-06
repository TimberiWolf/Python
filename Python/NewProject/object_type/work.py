'''
作业一
编写程序，实现如下功能，用户输入国家名称，打印所输入的国家名称和首都
'''

# country_city=dict(美国='纽约',日本='东京',中国='北京',英国='伦敦',巴西='里约热内卢',法国='巴黎',
#                   朝鲜='平壤',韩国='首尔',德国='柏林',俄罗斯='莫斯科',澳大利亚='堪培拉',意大利='罗马')
#
# country=input('请输入国家：')
# if country in country_city.keys():
#     city=country_city[country]
#     print(country,'==>',city)
# else:
#     print('您输入的国家不在查询范围内！')

'''
作业二
编写程序，实现用户输入数字，显示对应英文
'''

IntegerForLetter=dict((['0','zero'],['1','one'],['2','two'],['3','three'],['4','four'],
                       ['5','five'],['6','six'],['7','seven'],['8','eight'],['9','nine']))
number=input('Please input number:')
number_list=[]
if number.isdigit():
    for i in str(number):
        number_list.append(IntegerForLetter[i])
    number_word=' '.join(number_list)
    print(number,'==>',number_word)
else:
    print('请输入正确的数字！')
