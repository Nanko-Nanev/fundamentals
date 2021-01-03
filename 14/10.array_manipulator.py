def exchange(array, index):
    index = int(index)
    array_start = array[index+1:]
    array_end = array[0:index]
    return array_start + array_end


def even_or_odd_numbers(array, odd_or_even):
    array_list = []
    if odd_or_even == "even":
        for el in array:
            if el % 2 == 0:
                array_list.append(el)
    elif odd_or_even == "odd":
        for el in array:
            if not el % 2 == 0:
                array_list.append(el)

    if not array_list:
        print("No matches")
    else:
        return array_list


def first_last(array, first_or_last, odd_or_even, count):
    count = int(count)
    if count > len(array):
        print("Invalid count")
    array_list = even_or_odd_numbers(array, odd_or_even)
    if first_or_last == "first":
        if 0 < count < len(array_list):
            return array_list[0:count]
        else:
            return array_list
    elif first_or_last == "last":
        if 0 < count < len(array_list):
            return array_list[-count:]
        else:
            return array_list


array = input().split()
line = input()
while not line == "end":
    line = line.split()
    if line[0] == "exchange":
        array = exchange(array, line[1])
        print(array)
    elif line[0] == "max":
        print(max(even_or_odd_numbers(array, line[1])))
    elif line[0] == "min":
        print(min(even_or_odd_numbers(array, line[1])))
    elif line[0] == "first" or "last" == line[0]:
        print(first_last(array, line[0], line[2], line[1]))

    line = input()