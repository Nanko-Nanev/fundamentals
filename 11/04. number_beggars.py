numbers = input().split(",")
beggars = int(input())

list_of_sums = [0] * beggars

while numbers:
    for i in range(beggars):
        if numbers == []:
            break
        list_of_sums[i] += int(numbers.pop(0))

print(list_of_sums)
