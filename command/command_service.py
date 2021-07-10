from auth import AuthService
from command.command_repository import CommandRepository
from project.project_repository import ProjectRepository
from task.task_repository import TaskRepository
from user import UserRepository


class CommandService:
    def __init__(self):
        user_repository = UserRepository()
        auth_service = AuthService(user_repository)
        project_repository = ProjectRepository()
        task_repository = TaskRepository()
        self.commands = CommandRepository(auth_service, project_repository, task_repository).get_commands()

    def get_command(self, name):
        return self.commands.get(name)

    def execute_command(self, command_name):
        command1 = self.commands.get(command_name)
        if command1 is None:
            print("Command not exist")
        else:
            command1.action.__call__()
