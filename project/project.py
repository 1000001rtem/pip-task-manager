import uuid
from _datetime import datetime


class Project:
    def __init__(self, name, user_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.create_date = datetime.today()
        self.user_id = user_id

    def __str__(self):
        return "Project: " + self.name + " id: " + self.id
