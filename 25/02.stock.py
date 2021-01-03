dict_1 = {}
command = input().split()

for i in range(0, len(command), 2):
    food = command[i]
    quantity = command[i+1]
    dict_1[food] = int(quantity)

search = input().split()

for product in search:
    if product in dict_1:
        print(f"We have {dict_1[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")