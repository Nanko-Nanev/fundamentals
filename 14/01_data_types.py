def first_line_f(first_line_ff, second_line_f):
    if first_line_ff == "int":
        print(int(second_line_f) * 2)
    elif first_line_ff == "real":
        print(f"{(float(second_line_f) * 1.5):.2f}")
    elif first_line_ff == "string":
        print(f"${second_line_f}$")


first_line = input()
second_line = input()

first_line_f(first_line, second_line)