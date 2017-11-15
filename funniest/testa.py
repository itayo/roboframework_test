from robot.api.deco import keyword
from robot.api import logger
class testa(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = int(initial_amount)
    @keyword("Deposit to account a")
    def deposit(self, amount):
        self.balance += int(amount)
    @keyword("Withdraw from account a")
    def withdraw(self, amount):
        self.balance -= int(amount)

    @keyword("Balance account a")
    def dump(self):
        s = '%s, %s, balance: %s' % (self.name, self.no, self.balance)
        print s
        logger.warn(s)

