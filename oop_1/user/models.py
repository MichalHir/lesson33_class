class User:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    def __str__(self):
        return f"Name:{self.name}. Phone number:{self.phone_number}"