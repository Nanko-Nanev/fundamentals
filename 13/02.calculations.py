def custom_calc(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    if operator == "divide":
        result = int(a / b)
    if operator == "add":
        result = a + b
    if operator == "subtract":
        result = a - b
    return result


input_operator = input()
n1 = int(input())
n2 = int(input())

print(custom_calc(n1, n2, input_operator))