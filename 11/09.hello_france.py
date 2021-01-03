items = input().split("|")
budget = float(input())
invested_money = 0
list_of_new_prices = []

for item in items:
    item = item.split("->")
    if item[0] == "Clothes":
        if 1 <= float(item[1]) <= 50:
            if float(item[1]) <= budget:
                budget -= float(item[1])
                invested_money += float(item[1])
                list_of_new_prices.append(float(item[1]) * 1.4)
    elif item[0] == "Shoes":
        if 1 <= float(item[1]) <= 35:
            if float(item[1]) <= budget:
                budget -= float(item[1])
                invested_money += float(item[1])
                list_of_new_prices.append(float(item[1]) * 1.4)
    elif item[0] == "Accessories":
        if 1 <= float(item[1]) <= 20.5:
            if float(item[1]) <= budget:
                budget -= float(item[1])
                invested_money += float(item[1])
                list_of_new_prices.append(float(item[1]) * 1.4)

revenue = sum(list_of_new_prices)

for price in list_of_new_prices:
    print(f"{price:.2f} ", end="")
print()
profit = revenue - invested_money
print(f"Profit: {profit:.2f}")
if budget + revenue >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")
