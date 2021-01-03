list1 = input().split()
list1.sort(reverse=True)

for number in list1:
    print(f"{number}", end="")