dict_1 = {}
command = input().split(": ")
while not command[0] == "statistics":
    if command[0] not in dict_1:
        dict_1[command[0]] = int(command[1])
    else:
        dict_1[command[0]] += int(command[1])
    command = input().split(": ")

print(f"Products in stock:")
for product in dict_1:
    print(f"- {product}: {dict_1[product]}")
print(f"Total Products: {len(dict_1.keys())}")
print(f"Total Quantity: {sum(dict_1.values())}")