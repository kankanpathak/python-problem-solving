class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.__balance

account = BankAccount("Kankan", 5000)

account.deposit(1000)
account.withdraw(2000)

print(account.check_balance())
