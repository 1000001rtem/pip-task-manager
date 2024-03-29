from command import command


class CommandRepository:
    def __init__(self, auth_repository, project_repository, task_repository):
        self.commands = {}
        auth_service = auth_repository
        project_repository = project_repository
        task_repository = task_repository

        # service commands
        help_command = command.Command(
            command_name="help",
            description="Print all commands",
            secure=False,
            action=(
                lambda: print('\n'.join(map(lambda x: x.command_name + ": " + x.description, self.commands.values())))
            )
        )
        self.commands[help_command.command_name] = help_command

        # auth commands
        registration_command = command.Command(
            command_name="registration",
            description="Create new account",
            secure=False,
            action=(lambda: auth_service.registration(input("Username: "), input("Password: ")))
        )
        self.commands[registration_command.command_name] = registration_command

        login_command = command.Command(
            command_name="login",
            description="Enter to account",
            secure=False,
            action=(lambda: auth_service.login(input("Username: "), input("Password: ")))
        )
        self.commands[login_command.command_name] = login_command

        logout_command = command.Command(
            command_name="logout",
            description="Exit from account",
            secure=True,
            action=(lambda: auth_service.logout())
        )
        self.commands[logout_command.command_name] = logout_command

        self_command = command.Command(
            command_name="self",
            description="Print information about you",
            secure=True,
            action=(lambda: print(auth_service.get_current_user()))
        )
        self.commands[self_command.command_name] = self_command

        # project commands
        find_all_projects_command = command.Command(
            command_name="all_projects",
            description="Prints all your projects",
            secure=True,
            action=(lambda: print(
                '\n'.join(str(p) for p in project_repository.find_all(auth_service.current_user.id).values())))
        )
        self.commands[find_all_projects_command.command_name] = find_all_projects_command

        find_project_command = command.Command(
            command_name="find_project",
            description="Find project by ID",
            secure=True,
            action=(lambda: print(
                project_repository.find_project(auth_service.current_user.id, input("Please write ID: "))))
        )
        self.commands[find_project_command.command_name] = find_project_command

        create_project_command = command.Command(
            command_name="create_project",
            description="Create new project",
            secure=True,
            action=(lambda: project_repository.add_project(input("Please enter name: "), auth_service.current_user.id))
        )
        self.commands[create_project_command.command_name] = create_project_command

        delete_project_command = command.Command(
            command_name="delete_project",
            description="Delete project by ID",
            secure=True,
            # todo: удаление тасков
            action=(lambda: project_repository.delete_project(auth_service.current_user.id, input("Please write ID: ")))
        )
        self.commands[delete_project_command.command_name] = delete_project_command

        # task commands
        find_task_by_project_command = command.Command(
            command_name="task_by_project",
            description="Prints all task in project",
            secure=True,
            action=(lambda: print(
                '\n'.join(str(p) for p in task_repository.find_all_by_project(
                    auth_service.current_user.id,
                    input("Please write Project ID: ")
                ))))
        )
        self.commands[find_task_by_project_command.command_name] = find_task_by_project_command

        find_task_command = command.Command(
            command_name="find_task",
            description="Find task by ID",
            secure=True,
            action=(lambda: print(
                task_repository.find_task(auth_service.current_user.id, input("Please write ID: "))))
        )
        self.commands[find_task_command.command_name] = find_task_command

        create_task_command = command.Command(
            command_name="create_task",
            description="Create new task",
            secure=True,
            action=(lambda: task_repository.add_task(
                input("Please enter name: "),
                auth_service.current_user.id,
                input("Please enter project ID: ")
            ))
        )
        self.commands[create_task_command.command_name] = create_task_command

        delete_task_command = command.Command(
            command_name="delete_task",
            description="Delete task by ID",
            secure=True,
            action=(lambda: task_repository.delete_task(auth_service.current_user.id, input("Please write ID: ")))
        )
        self.commands[delete_task_command.command_name] = delete_task_command

    def get_commands(self):
        return self.commands
