def case(username, command):
    if command == "lower":
        username = user_name.lower()
    elif command == "upper":
        username = user_name.upper()
    return username


def reverse(start_index, end_index, username):
    if 0 < start_index < len(username)-1:
        if start_index < end_index < len(username)-1:
            reversed_string = username[end_index:start_index-1:-1]
            print(reversed_string)


def cut(substring, username):
    if substring in username:
        username = username.replace(substring, "")
        return username
    else:
        print(f"The word {username} doesn't contain {substring}.")


def replace(char, username):
    username = username.replace(char, "*")
    return username


def check(char):
    if char in user_name:
        print(f"Valid")
    else:
        print(f"Your username must contain {char}.")


user_name = input()
string = input()

while not string == "Sign up":
    string = string.split()
    if string[0] == "Case":
        user_name = case(user_name, string[1])
        print(user_name)
    elif string[0] == "Reverse":
        reverse(int(string[1]), int(string[2]), user_name)
    elif string[0] == "Cut":
        if not cut(string[1], user_name) is None:
            user_name = cut(string[1], user_name)
            print(user_name)
    elif string[0] == "Replace":
        user_name = replace(string[1], user_name)
        print(user_name)
    elif string[0] == "Check":
        check(string[1])

    string = input()