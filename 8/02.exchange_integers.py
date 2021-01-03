n1 = int(input())
n2 = int(input())

print("Before:")
print(f"a = {n1}")
print(f"b = {n2}")

n1, n2 = n2, n1

print("After:")
print(f"a = {n1}")
print(f"b = {n2}")
