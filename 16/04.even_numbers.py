command = input().split(", ")
result = []

for i in range(len(command)):
    if int(command[i]) % 2 == 0:
        result.append(i)

print(result)