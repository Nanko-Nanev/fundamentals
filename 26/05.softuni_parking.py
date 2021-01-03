class Parking:
    def __init__(self, name, plate=None):
        self.name = name
        self.plate = plate

    def register(self, register_name, register_plate):
        if register_name in list_of_names:
            print(f"ERROR: already registered with plate number {register_plate}")
        else:
            list_of_names[register_name] = register_plate
            print(f"{register_name} registered {register_plate} successfully")

    def unregister(self, unregister_name):
        if unregister_name not in list_of_names:
            print(f"ERROR: user {unregister_name} not found")
        else:
            list_of_names.pop(unregister_name)
            print(f"{unregister_name} unregistered successfully")


n = int(input())
list_of_names = {}


for i in range(n):
    command = input().split()
    if command[0] == "register":
        parking = Parking(command[1], command[2])
        parking.register(command[1], command[2])
    elif command[0] == "unregister":
        parking = Parking(command[1])
        parking.unregister(command[1])

for names in list_of_names:
    print(f"{names} => {list_of_names[names]}")