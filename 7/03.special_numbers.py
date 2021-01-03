n = int(input())

for i in range(1, n+1):
    number = i
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number = int(number / 10)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")