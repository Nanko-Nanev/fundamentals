command = input().split()
result = ""

for word in command:
    result += word * (len(word))

print(result)

