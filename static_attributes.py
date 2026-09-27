#static attributes vs instance attributes

#static = belongs to class, not object of the class
#are shared by all instances of the class
#created once at the CLASS LEVEL



class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1


    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1 = User("dan", "dan@gmail.com")
user2 = User("alex", "alex@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)

#Static vs instance method example
class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount): 
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("deposit must be positive")

    def _is_valid_amount(self, amount):
        return amount > 0 #protected method

    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: {self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)

account.__log_transaction("withdraw", 300)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))

    


