def repeat(string, times):
    result = ""
    for i in range(times):
        result += string
    return result


string_input = input()
repeat_times = int(input())

print(repeat(string_input, repeat_times))