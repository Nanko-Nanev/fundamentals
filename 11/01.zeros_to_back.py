zero_to_back = input().split(", ")

zero_to_back = [int(number) for number in zero_to_back]

for i in range(len(zero_to_back)):
    if zero_to_back[i] == 0:
        zero_to_back.remove(zero_to_back[i])
        zero_to_back.append(0)

print(zero_to_back)
