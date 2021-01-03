# Type of fire
high_fire = range(81, 125+1)
medium_fire = range(51, 80+1)
low_fire = range(1, 50+1)

effort = 0
cells_put_out = []
total_fire = 0

cell_with_fires = input().split("#")
water = int(input())

for cell in cell_with_fires:
    cell = cell.split(" = ")
    if cell[0] == "High":
        if int(cell[1]) in high_fire:
            if water >= int(cell[1]):
                water -= int(cell[1])
                effort += int(cell[1]) * 0.25
                cells_put_out.append(cell[1])
                total_fire += int(cell[1])
    if cell[0] == "Medium":
        if int(cell[1]) in medium_fire:
            if water >= int(cell[1]):
                water -= int(cell[1])
                effort += int(cell[1]) * 0.25
                cells_put_out.append(cell[1])
                total_fire += int(cell[1])
    if cell[0] == "Low":
        if int(cell[1]) in low_fire:
            if water >= int(cell[1]):
                water -= int(cell[1])
                effort += int(cell[1]) * 0.25
                cells_put_out.append(cell[1])
                total_fire += int(cell[1])

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")