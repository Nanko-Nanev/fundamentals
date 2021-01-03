lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
games = 0
broken_shields = 0

while not games == lost_fights_count:
    games += 1
    if games % 2 == 0:
        expenses += helmet_price
    if games % 3 == 0:
        expenses += sword_price
        if games % 2 == 0:
            expenses += shield_price
            broken_shields += 1
            if broken_shields == 2:
                broken_shields = 0
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")