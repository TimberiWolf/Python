'''
计算两个个日期相差多少天
'''

import datetime
from dateutil import rrule

class BetDate:
    def __init__(self,start_date,stop_date):
        self.start=datetime.datetime.strftime(start_date,fmt='%Y-%m-%d')
        self.stop=datetime.datetime.strftime(stop_date,fmt='%Y-%m-%d')

    def days(self):
        d = self.stop - self.start
        return d.days if d.days>0 else False

    def weeks(self):
        weeks=rrule.rrule(rrule.WEEKLY,dtstart=self.start,until=self.stop)
        return weeks.count()

fir_twe=BetDate(2019-5-1,2019-11-29)
d=fir_twe.days()
w=fir_twe.weeks()
print('Between 2019-5-1,2019-11-15:')
print('Days is:',d)
print('Weeks is:',w)


#需要调试，先不处理