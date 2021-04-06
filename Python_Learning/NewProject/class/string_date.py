'''
创建一个类，判断日期格式是否合法，‘Y-m-d’
'''

class Date:
    def __init__(self,year=0,month=0,day=0):
        self.year=year
        self.month=month
        self.day=day

    @classmethod
    def from_string(cls,date_as_string):
        year,month,day=map(int,date_as_string.split('-'))
        date1=cls(year,month,day)
        return date1

    @staticmethod
    def date_is_valid(date_as_string):
        year,month,day=map(int,date_as_string.split('-'))
        # a=1
        # a= month==2 and day <= 29
        a = month != 2 or month ==2 and day<=29 and year%4==0
        # if month==2 and day>29:
        #     a=False
        # else:
        #     a=True

        return day<=31 and month<=12 and year<=2038 and a

d=Date.from_string('2020-12-14')
is_date=Date.date_is_valid('2021-2-29')
print(is_date)