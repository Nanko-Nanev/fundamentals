targets = input().split()
targets = [int(target) for target in targets]

line = input()

while not line == "End":
    line = line.split()
    if line[0] == "Shoot":
        index = int(line[1])
        power = int(line[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                del targets[index]
                #targets.remove(index)
                #targets[index] = 0 # remove target

    elif line[0] == "Add":
        index = int(line[1])
        value = int(line[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif line[0] == "Strike":
        index = int(line[1])
        strike_radius = int(line[2])
        if 0 <= index < len(targets):
            if (0 <= (index - strike_radius)) and ((index + strike_radius) < len(targets) -1):
                for i in range(index - strike_radius, index + strike_radius + 1):
                    targets[i] = 0

            else:
                print("Strike missed!")
        else:
            print("Strike missed!")
        for el in targets:
            if el == 0:
                targets.remove(el)

    line = input()

for el in targets:
    if el == 0:
        targets.remove(el)

targets = [str(el) for el in targets]
print("|".join(targets))