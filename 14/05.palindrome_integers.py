def palindrome_checker(a):
    for i in a:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


input_string = input().split(", ")
palindrome_checker(input_string)


