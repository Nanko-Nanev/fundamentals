def move_left(index, movable_list: list):
    if index == 0 or index > len(movable_list) - 1:
        pass
    else:
        movable_list.insert(index - 1, movable_list.pop(index))


def move_right(index, movable_list: list):
    if index >= len(movable_list) - 1:
        pass
    else:
        movable_list.insert(index + 1, movable_list.pop(index))


def check_even(list_of_things):
    result = ""
    odd = False
    for part in list_of_things:
        if not odd:
            result += part + " "
            odd = True
        else:
            odd = False
    print(result[:-1])


def check_ood(list_of_things):
    result = ""
    odd = False
    for part in list_of_things:
        if odd:
            result += part + " "
            odd = False
        else:
            odd = True
    print(result[:-1])


name_parts = input().split("|")
whole_name = ""
program_working = True

while program_working:
    command_tokens = input().split(" ")
    if command_tokens[0] == "Move":
        if command_tokens[1] == "Left":
            move_left(int(command_tokens[2]), name_parts)
        if command_tokens[1] == "Right":
            move_right(int(command_tokens[2]), name_parts)
    if command_tokens[0] == "Done":
        for word in name_parts:
            whole_name += word
        print(f"You crafted {whole_name}!")
        program_working = False
    if command_tokens[0] == "Check":
        if command_tokens[1] == "Even":
            check_even(name_parts)
        if command_tokens[1] == "Odd":
            check_ood(name_parts)
