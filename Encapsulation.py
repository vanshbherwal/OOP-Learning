# Encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1

print(account.balance)

class BankAccount:

    def __init__(self):
        self._balance = 0.0 #made it a protected attribute

    @property
    def balance(self):
        return self._balance #provides controlled access to protected balance data

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        if amount >= self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount


goodAccount = BankAccount()
print(goodAccount.balance) #calling property method
goodAccount.deposit(1.99)
print(goodAccount.balance)
goodAccount.withdraw(1)
print(goodAccount.balance)




