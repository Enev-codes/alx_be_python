class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = 0

    def deposit(self, amount):
        return (self.account_balance + amount)

    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: $[{self.account_balance}]")

