class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def check_balance(self):
        return self.balance

    def transfer(self, amount, another_account):
        if self.balance >= amount:
            self.balance -= amount
            another_account.balance += amount


account1 = BankAccount("Rahul", 5000)

account2 = BankAccount("Priya", 3000)

account1.deposit(1000)
account1.withdraw(500)

account1.transfer(2000, account2)

print(account1.check_balance())
print(account2.check_balance())
