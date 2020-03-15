class NotSecureCommandService:
    def __init__(self, user_id):
        self.commands = {}

        # service commands
        self.commands["help"] = "Print all commands", (
            lambda: print('\n'.join(map(lambda x: x[0] + " -> " + x[1][0], self.commands.items()))))

    def get_command(self, name):
        return self.commands.get(name)[1]
