n = int(input())
capacity = 255
current_liters = 0

for i in range(n):
    liters = int(input())
    if current_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        current_liters += liters
print(f"{current_liters}")