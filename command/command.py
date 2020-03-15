class Command:
    def __init__(self, command_name, description, secure, action):
        self.command_name = command_name
        self.description = description
        self.secure = secure
        self.action = action

