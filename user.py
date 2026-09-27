from datetime import datetime

class User:

    def __init__(self, username, email, password):

        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

user1 = User("dan", "dan@gmail.com", "123")
#user1.email = "this is not an email"
print(user1.get_email())

user1.set_email("12@34")
print(user1.get_email())






