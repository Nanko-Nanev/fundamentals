number = int(input())
total_sum = 0

for i in range(number):
    char = input()
    char = ord(char)
    total_sum += char

print(f"The sum equals: {total_sum}")