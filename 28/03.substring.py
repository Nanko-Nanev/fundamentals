remove_command = input()
command = input()

while remove_command in command:
    command = command.replace(remove_command, "")

print(command)