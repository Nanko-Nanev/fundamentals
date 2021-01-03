to_do_list = [0] * 11
comand = input().split("-")

while not comand[0] == "End":
    to_do_list[int(comand[0])] = comand[1]
    comand = input().split("-")

result = []
for task in to_do_list:
    if not task == 0:
        result.append(task)

print(result)