version = input().split(".")

map_object = map(int, version)
version = list(map_object)

version[2] += 1

if version[2] == 10:
    version[1] += 1
    version[2] = 0

if version[1] == 10:
    version[0] += 1
    version[1] = 0

print(f"{version[0]}.{version[1]}.{version[2]}")
