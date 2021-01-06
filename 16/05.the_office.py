happiness = input().split()
factor = int(input())

happiness = list(map(lambda x: int(x) * factor, happiness))

average = sum(happiness) / len(happiness)

happy = []
unhappy = []

for el in happiness:
    if el >= average:
        happy.append(el)
    else:
        unhappy.append(el)

if len(happy) >= len(unhappy):
    print(f"Score: {len(happy)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{len(happiness)}. Employees are not happy!")