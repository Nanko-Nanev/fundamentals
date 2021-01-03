def perfect_number_check(n):
    n2 = n/2
    sum_of_numbers = 0
    for i in range(1, int(n2+1)):
        if n % i == 0:
            sum_of_numbers += i

    if n == sum_of_numbers:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())
perfect_number_check(n)