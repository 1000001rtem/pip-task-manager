import uuid


class User:
    def __init__(self, name, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.password = password

    def __str__(self):
        return self.id + " " + self.name
