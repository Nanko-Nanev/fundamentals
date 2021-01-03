import math

def roundup(max_number):
    return int(math.ceil(max_number/10.0)) * 10


numbers = input().split(", ")
numbers = [int(i) for i in numbers]
groups_number = roundup(max(numbers))
group_index = 10
current_list = []

while not numbers == []:
    for number in numbers:
        if number <= group_index:
            current_list.append(number)
    for number in numbers[:]:
        if number in current_list:
            numbers.remove(number)
    print(f"Group of {group_index}'s: {current_list}")
    current_list = []
    group_index += 10