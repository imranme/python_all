# ১. ব্যাংক অ্যাকাউন্ট সিস্টেম

# একটি BankAccount ক্লাস বানাও, যেখানে টাকা জমা (deposit), টাকা উত্তোলন (withdrawal) এবং ব্যালেন্স চেক করার ব্যবস্থা থাকবে।
# এরপর এটিকে দুইভাবে বাড়াও:

# SavingsAccount → এখানে সুদের (interest) হিসাব থাকবে।

# CurrentAccount → এখানে ওভারড্রাফট (overdraft) সীমা থাকবে।

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def witdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("empty money")
        return self.balance
    
    def check_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate = 0.05):
        super().__init__(balance)
        self.interest_rest = interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.interest_rest
        return self.balance
    
acc = SavingsAccount(1000)
print("strat:", acc.check_balance())
acc.deposit(500)
print("after dipojit:", acc.check_balance())
acc.add_interest()
print("after add interaste:", acc.check_balance())
