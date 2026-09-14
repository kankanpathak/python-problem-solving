class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def display_balance(self):
        return f"Account holder: {self.account_holder}\nAvailable balance: {self.balance}"


BankAccount1 = BankAccount("Rahul", 5000)

BankAccount1.deposit(1500)
BankAccount1.withdraw(2000)
BankAccount1.withdraw(6000)
print(BankAccount1.display_balance())
