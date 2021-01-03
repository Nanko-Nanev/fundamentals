dict = {}
command = input().split()

for i in range(0, len(command), 2):
    food = command[i]
    quantity = command[i+1]
    dict[food] = int(quantity)

print(dict)
