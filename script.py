class Dog:

    def __init__(self, name, breed, owner): #only ran once when method is instantiated
        self.name = name
        self.breed = breed
        self.owner = owner


    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name 
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("Danny", "122 Springfield Drive", "123-456-7890")

dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)

dog2 = Dog("Derek", "English Labrador", owner1)
print(dog2.owner.name)


    

