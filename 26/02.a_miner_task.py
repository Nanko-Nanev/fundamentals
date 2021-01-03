command = input()
result = {}
while not command == "stop":
    if command not in result:
        result[command] = int(input())
    else:
        result[command] += int(input())
    command = input()

for resource in result:
    print(f"{resource} -> {result[resource]}")