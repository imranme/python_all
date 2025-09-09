import datetime
import random

class BkashAccount:
    def __init__(self, name, phone, balance=0):
        self.name = name
        self.phone = phone
        self.__balance = balance   # ✅ Private balance

    # Q1: Print object details
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Balance: {self.__balance} Tk"

    # Balance secure access
    def get_balance(self):
        return self.__balance

    # Internal method to update balance (not accessible outside)
    def __update_balance(self, amount):
        self.__balance += amount

    # OTP Generator
    def generate_otp(self):
        return random.randint(1000, 9999)

    # Common transaction method
    def transaction(self, amount, txn_type, receiver=None):
        if txn_type != "Cash In" and self.__balance < amount:
            return "❌ Insufficient Balance!"
        
        # OTP Verification
        otp = self.generate_otp()
        print(f"OTP sent: {otp}")
        user_otp = int(input("Enter OTP: "))
        if user_otp != otp:
            return "❌ Transaction Failed! Invalid OTP."
        
        # Update Balance
        if txn_type == "Cash In":
            self.__update_balance(amount)
        else:
            self.__update_balance(-amount)

        # Transaction details
        txn_id = random.randint(100000, 999999)
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        details = {
            "Transaction ID": txn_id,
            "Date": date_time,
            "Type": txn_type,
            "Amount": amount,
            "Receiver": receiver if receiver else "N/A",
            "Current Balance": self.__balance
        }
        return details

    # Q2: Send Money
    def send_money(self, receiver_number, amount):
        return self.transaction(amount, "Send Money", receiver_number)

    # Q3: Cash Out
    def cash_out(self, agent_number, amount):
        return self.transaction(amount, "Cash Out", agent_number)

    # Cash In
    def cash_in(self, amount):
        return self.transaction(amount, "Cash In")
