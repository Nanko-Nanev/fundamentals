string_number = input()
new_list = []

list_numbers = string_number.split()
for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i]) * -1

print(list_numbers)