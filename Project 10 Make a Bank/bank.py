'''
Account class
This class is the abstrated basic elements of an account
'''
class Account:
    def __init__(self,accountName,accountBalance,accountMinBalance):
        self.accountName = accountName
        self.accountBalance = accountBalance
        self.accountMinBalance = accountMinBalance
'''
the deposit action within all accounts
'''
    def deposit(self,amount):
        self.accountBalance += amount
'''
all accounts can have a withdraw feature
'''
    def withdraw(self,amount):
        if self.accountBalance - amount >= self.accountMinBalance:
            self.accountBalance -= amount
        else:
            print("Sorry not enough funds!")
'''
all accounts can print a statement
'''
    def statement(self):
        print("Account Balance:$ {}".format(self.accountBalance))
'''
This will be a live checking(Current) account
'''
class CurrentAccount(Account):
    def __init__(self,accountName,accountBalance):
        super().__init__(accountName,accountBalance,accountMinBalance= -1000)

    def __str__(self):
        return"{}'s current account: Balance ${}".format(self.accountName,self.accountBalance)
'''
A live Savings account 
'''
class Savings(Account):
    def __init__(self,accountName,accountBalance):
        super().__init__(accountName,accountBalance,accountMinBalance= 0)

    def __str__(self):
        return "{}'s Savings account: Balance ${}".format(self.accountName, self.accountBalance)



x = CurrentAccount("Phillip",500)
x.deposit(300)
x.withdraw(600)
x.statement()
print(x)
