from datetime import datetime


class User():

    def __init__(self, name, email, password) -> None:
        name = name
        email = email
        password = password

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "email": self.email,
            "password": self.password,
            "date_created": datetime.now()
        }