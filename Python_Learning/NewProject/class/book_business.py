'''
编写程序，根据图书的单价，购买数量以及快递费，计算卖家应支付的总额
'''

class Buyer:

    def __init__(self,name,price,numbers):
        self.name=name
        self.price=price
        self.number=numbers

    def get_pay(self):
        order_amount=self.price*self.number
        if order_amount < 30:
            order_amount+=5
        else:
            pass
        return order_amount

laowang=Buyer('laowang',5,10)
laowang_pay=laowang.get_pay()
print('{0} should pay:{1}'.format(laowang.name,laowang_pay))

laozhang=Buyer('laozhang',3,9)
laozhang_pay=laozhang.get_pay()
print('{0} should pay:{1}'.format(laozhang.name,laozhang_pay))
