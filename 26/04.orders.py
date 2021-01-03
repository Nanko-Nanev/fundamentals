products_price = {}
products_quantities = {}

command = input()

while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products_price:
        products_price[name] = price
        products_quantities[name] = quantity
    else:
        products_price[name] = price
        products_quantities[name] += quantity

    command = input()

for name in products_price:
    total_price = products_price[name] * products_quantities[name]
    print(f"{name} -> {total_price:.2f}")