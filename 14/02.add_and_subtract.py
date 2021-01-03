def sum_numbers(num1, num2):
    num4 = num1 + num2
    return num4


def subtract(num4, num3):
    num5 = num4 - num3
    return num5


def add_and_subtract(a):
    print(a)


n1 = int(input())
n2 = int(input())
n3 = int(input())

add_and_subtract(subtract(sum_numbers(n1, n2), n3))
