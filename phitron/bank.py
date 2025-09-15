class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.main_balance= 1000
        self.max_balance = 20000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount < self.main_balance:
            print(f'bank fokir hoye jabe, you van not with more then{self.main_balance}')
        elif amount > self.max_balance:
            print(f'bank taka nay{self.max_balance}')
        else:
            self.balance -= amount
            print(f'here is your money{amount}')

brac = Bank(2344)
brac.withdraw(25)
brac.withdraw(324234234)
brac.withdraw(4334)


city = Bank(3000)
city.withdraw(23)
city.withdraw(30000)