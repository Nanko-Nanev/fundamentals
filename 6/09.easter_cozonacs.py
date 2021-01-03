budget = float(input())
price_for_1_kg_of_flour = float(input())
price_for_1_pack_of_eggs = 0.75 * price_for_1_kg_of_flour
price_for_1l_milk = price_for_1_kg_of_flour * 1.25
price_for_1_cozonac = price_for_1_kg_of_flour + price_for_1_pack_of_eggs + (price_for_1l_milk * 0.25)
cozonacs_count = 0
colored_eggs = 0

while budget >= price_for_1_cozonac:
    budget -= price_for_1_cozonac
    if budget >= 0:
        cozonacs_count += 1
        colored_eggs += 3
    else:
        break
    if cozonacs_count % 3 == 0:
        colored_eggs -= cozonacs_count - 2

print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")