line = input()
power = 0

for i in range(len(line)):
    c = line[i]
    if c == ">":
        if line[i + 1].isdigit():
            power += int(line[i+1])
    elif power > 0:
        line = line[:i] + "x" + line[i + 1:]
        power -= 1

print(line.replace("x", ""))