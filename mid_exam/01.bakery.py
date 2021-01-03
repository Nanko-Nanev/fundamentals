import math

biscuits_produced_per_day_per_worker = int(input())
workers_count = int(input())
number_of_biscuits_of_competing_factory_for_30_days = int(input())
total_biscuits_produced = 0
third_day_checker = 0

for i in range(30):
    third_day_checker += 1
    if third_day_checker == 3:
        third_day_checker = 0
        total_biscuits_produced += math.floor(((biscuits_produced_per_day_per_worker * workers_count) * 0.75))
    else:
        total_biscuits_produced += (biscuits_produced_per_day_per_worker * workers_count)

print(f"You have produced {total_biscuits_produced} biscuits for the past month.")

difference = total_biscuits_produced - number_of_biscuits_of_competing_factory_for_30_days
percentage = difference / number_of_biscuits_of_competing_factory_for_30_days * 100

if percentage < 0:
    print(f"You produce {percentage*-1:.2f} percent less biscuits.")
else:
    print(f"You produce {percentage:.2f} percent more biscuits.")