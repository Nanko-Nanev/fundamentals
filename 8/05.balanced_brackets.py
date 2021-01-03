number_of_lines = int(input())
open_brackets = 0
close_brackets = 0
opening = 0

for i in range(number_of_lines):
    line = input()
    if line == "(":
        open_brackets += 1
        opening += 1
    elif line == ")":
        close_brackets += 1
        opening = 0
    if opening == 2:
        break

if close_brackets == open_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")