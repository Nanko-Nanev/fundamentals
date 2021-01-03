command = input().split()
str1 = command[0]
str2 = command[1]
total_sum = 0

for i in range(min((len(str1), len(str2)))):
    total_sum += ord(str1[i]) * ord(str2[i])

if not len(str1) == len(str2):
    if len(str1) > len(str2):
        for i in range(len(str2), len(str1)):
            total_sum += ord(str1[i])
    else:
        for i in range(len(str1), len(str2)):
            total_sum += ord(str2[i])

print(total_sum)
