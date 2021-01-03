command = input().split("\\")
name_extension = command[-1]
name, extension = name_extension.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")