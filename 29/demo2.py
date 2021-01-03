line = input()

strength = 0
index = 0

while index < len(line):

    if line[index] == ">":
        index += 1
        if line[index + 1].isdigit():
            strength += int(line[index + 1])
        else:
            strength += int(line[index])
        while not line[index] == ">" and not strength == 0:
            line = line[:index] + line[index + 1:]
            strength -= 1
    else:
        index += 1

print(line)