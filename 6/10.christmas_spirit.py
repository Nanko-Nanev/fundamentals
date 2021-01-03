allowed_quantity = int(input())
days = int(input())
christmas_spirit = 0
total_cost = 0

for day in range(1, days+1):
    if day % 11 == 0:
        allowed_quantity += 2
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 5 + 3 + 15
        if day == days:
            christmas_spirit -= 30
    if day % 5 == 0:
        total_cost += 15 * allowed_quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 3 == 0:
        total_cost += (5 * allowed_quantity)+(3 * allowed_quantity)
        christmas_spirit += 13
    if day % 2 == 0:
        total_cost += 2 * allowed_quantity
        christmas_spirit += 5

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")