import user
import project
import auth
from command.command_repository import CommandRepository


class CommandService:
    def __init__(self):
        user_repository = user.user_repository.UserRepository()
        auth_service = auth.AuthService(user_repository)
        project_repository = project.project_repository.ProjectRepository()
        self.commands = CommandRepository(auth_service, project_repository).get_commands()

    def get_command(self, name):
        return self.commands.get(name)

    def execute_command(self, command_name):
        command1 = self.commands.get(command_name)
        if command1 is None:
            print("Command not exist")
        else:
            command1.action.__call__()
