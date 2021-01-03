def loading_bar(n):
    loading_string = ("%" * int(n / 10)) + ("." * int(10 - n/10))
    return loading_string


n = int(input())

if n == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    print(f"{n}% [{loading_bar(n)}]")
    print("Still loading...")