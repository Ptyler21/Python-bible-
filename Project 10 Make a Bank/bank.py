
#A class named 'Account'
#A class for elements that ALL accounts have
'''
Abstraction: Account
'''
class Account:
    def __init__(self,accountName,accountBalance,accountMinBalance):
        self.accountName = accountName
        self.accountBalance = accountBalance
        self.accountMinBalance = accountMinBalance

#A function for an action related to an account
'''
Action: Deposit
while performing a deposit: AMOUNT of money, ACCOUNT TYPE

'''
    def deposit(self,amount):
        self.accountBalance += amount

'''
Action: withdraw
anyone can withdraw money from either account
-you must have enough money
-overdraft fees
'''
    def withdraw(self,amount):
        if amount >= self.accountMinBalance:
            self.accountBalance -= amount

        else:
            print("Not enough money available!")
'''
'Action: generate a statement'
'''
    def statement(self):
        print("Account Balance: {}".format(self.accountBalance))
