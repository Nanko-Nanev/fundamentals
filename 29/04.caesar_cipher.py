command = input()
result = ""
for char in command:
    result += chr(ord(char)+3)

print(result)