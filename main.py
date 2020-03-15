import command
import auth

print("Welcome to Pip Task Manager")
print("For exit write 'exit'")
print("For help write 'help'")
flag = True
command_service = command.CommandService()
current_user = None

while flag:
    command_name = input("Please enter your command: ")
    if command_name == "exit":
        flag = False
        continue

    command_service.execute_command(command_name)

print("Bye Bye!")
