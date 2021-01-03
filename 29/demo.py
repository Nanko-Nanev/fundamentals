line = input()

index = 0
strength = 0

while index < len(line):
    if line[index] == ">":
        strength += int(line[index + 1])
        if strength <= 2:
            index += 1
        while not line[index] == ">" and strength:
            line = line.replace(line[index], "", 1)
            strength += 1
    else:
        index += 1

# string = input()
# print("".join([symbol for index, symbol in enumerate(string)if index == 0 or symbol != string[index - 1]]))