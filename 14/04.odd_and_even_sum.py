def sum_of_odd_and_even_numbers(a):
    odd = 0
    even = 0
    for i in a:
       if int(i) % 2 == 0:
           even += int(i)
       else:
           odd += int(i)
    print(f"Odd sum = {odd}, Even sum = {even}")


input1 = input()
sum_of_odd_and_even_numbers(input1)