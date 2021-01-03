import re

data = input()
pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"

while data:
    for el in re.finditer(pattern, data):
        print(el.group())

    data = input()



