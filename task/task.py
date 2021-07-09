import uuid
from _datetime import datetime


class Task:
    def __init__(self, name, user_id, project_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.create_date = datetime.today()
        self.user_id = user_id
        self.project_id = project_id

    def __str__(self):
        return "Task: " + self.name + " id: " + self.id + " project: " + self.project_id
