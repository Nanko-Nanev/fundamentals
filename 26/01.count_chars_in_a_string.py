command = input()
result = {}

for char in command:
    if ord(char) == 32:
        continue
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1

for char in result:
    print(f"{char} -> {result[char]}")