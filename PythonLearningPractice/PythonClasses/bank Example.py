import sys
class Bank:
    '''this class is doing deposit and withdraws operation'''

    bank = 'welcome to sbi'

    def __init__(self,name, bal=o):
        self.name = name
        self.bal = bal

    def deposit (self,amt):
        self.bal = self.bal + amt
        print (' balance is ',self.bal)

    def withdraw (self, amt):
        if amt > self.bal
            print('insufficient balance')
            sys.exit
c=Bank()
c.bank
while True:
    option=print('what operation u want to perform ')
