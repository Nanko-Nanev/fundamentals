n = int(input())
result = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in result:
        result[word] = []
    result[word].append(synonym)

for word in result:
    print(f"{word} - {', '.join(result[word])}")