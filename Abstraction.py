# Abstraction
# Reduces complexity by hiding unnecessary details

class EmailService:
    
    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server") #_method are protected methods that are just for internal development

email = EmailService()
email.send_email() 


#Encapsulation focuses on bundling data and methods and restricts access to internal development details. This is achieved by labeling methods as protected or private. 

#Encapsulation is a process that enables Abstraction