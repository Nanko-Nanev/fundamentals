line_with_words = input().lower().split()
result = {}

for word in line_with_words:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1

for (key, value) in result.items():
    if not value % 2 == 0:
        print(f"{key}", end=" ")