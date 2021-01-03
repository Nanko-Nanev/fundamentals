vehicles = input().split(", ")
n = int(input())

for i in range(n):
    commands = input().split(", ")
    if commands[0] == "Add":
        if commands[1] in vehicles:
            print("Card is already bought")
        else:
            print("Card successfully bought")
            vehicles.append(commands[1])
    elif commands[0] == "Remove":
        if commands[1] in vehicles:
            print("Card successfully sold")
            vehicles.remove(commands[1])
        else:
            print("Card not found")
    elif commands[0] == "Remove At":
        if int(commands[1]) <= len(vehicles) - 1:
            vehicles.pop(int(commands[1]))
            print("Card successfully sold")
        else:
            print("Index out of range")
    elif commands[0] == "Insert":
        if int(commands[1]) <= len(vehicles) - 1:
            if commands[2] in vehicles:
                print("Card is already bought")
            else:
                vehicles.insert(int(commands[1]), commands[2])
                print("Card successfully bought")
        else:
            print("Index out of range")

for i in range(len(vehicles)-1):
    print(f"{vehicles[i]}", end=", ")

print(f"{vehicles[-1]}")