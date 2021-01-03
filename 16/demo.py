wagons = int(input())
wagons_list = [0] * wagons

comand = input()
comand.split()

if comand[0] == "add":
    wagons_list[-1] += int(comand[1])
    print(wagons_list)