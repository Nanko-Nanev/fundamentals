command = input()
companies = {}

while not command == "End":
    name, ids = command.split(" -> ")

    if name not in companies:
        companies[name] = []
    if ids not in companies[name]:
        companies[name].append(ids)

    command = input()

for name, ids in sorted(companies.items(), key=lambda x: x[0]):
    print(name)
    for e_id in ids:
        print(f"-- {e_id}")



#     companies[name] = list(ids)
#
#
# print(companies)
# for key, values in companies.items():
#     print(f"{key}")
#     for i in range(len(companies[values])):
#         print(f"-- {companies[i]}")