def factorial(n):
    factorial_n = 1
    for i in range(n, 1, -1):
        factorial_n *= i
    return factorial_n


n1 = int(input())
n2 = int(input())

print(f"{(factorial(n1) / factorial(n2)):.2f}")