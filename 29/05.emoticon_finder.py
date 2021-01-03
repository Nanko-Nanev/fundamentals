command = input().split()

for char in command:
    for i in range(len(char)):
        if char[i] == ":":
            print(f"{char[i:i+2]}")