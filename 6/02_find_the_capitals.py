word = input()
word_list = []

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        word_list.append(i)

print(word_list)