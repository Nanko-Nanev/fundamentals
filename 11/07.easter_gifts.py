gifts = input().split()
line = input()
while not line == "No Money":
    line = line.split()
    if line[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == line[1]:
                gifts[i] = None
    if line[0] == "Required":
        if 0 <= int(line[2]) <= (len(gifts) - 1):
            gifts[int(line[2])] = line[1]
    if line[0] == "JustInCase":
        gifts[-1] = line[1]

    line = input()

for gift in gifts:
    if not gift == None:
        print(f"{gift} ", end="")
