wagons = int(input())
wagons_list = [0] * wagons
comand = input().split()

while not comand[0] == "End":
    if comand[0] == "add":
        wagons_list[-1] += int(comand[1])
    elif comand[0] == "insert":
        wagons_list[int(comand[1])] += int(comand[2])
    elif comand[0] == "leave":
        wagons_list[int(comand[1])] -= int(comand[2])
    comand = input().split()

print(wagons_list)