def total_price(product, quantity):
    total_p = 0
    if product == "coffee":
        total_p = quantity * 1.50
    if product == "water":
        total_p = quantity * 1.00
    if product == "coke":
        total_p = quantity * 1.40
    if product == "snacks":
        total_p = quantity * 2.00
    return total_p


food = input()
quantity_input = int(input())

print_total_price = total_price(food, quantity_input)
print(f"{print_total_price:.2f}")