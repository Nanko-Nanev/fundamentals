n = int(input())
battle_field = []
field_widnes = 0
zero_count_start = 0
zero_count_end = 0
ships_destroyed = 0

for i in range(n):
    battle_field += input().split()

battle_field = [int(field) for field in battle_field]

field_widnes = int(len(battle_field) / n)
attacks = input().split()

zero_count_start = battle_field.count(0)

for each_attack in attacks:
    row, col = each_attack.split("-")
    row = int(row)
    col = int(col)
    attack = (row * field_widnes) + col
    if battle_field[attack] > 0:
        battle_field[attack] -= 1
        if battle_field[attack] == 0:
            ships_destroyed += 1

zero_count_end = battle_field.count(0)
# print(zero_count_end - zero_count_start)
print(ships_destroyed)