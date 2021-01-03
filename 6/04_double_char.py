word = input()
new_word = ""

for i in range(len(word)):
    new_word += word[i] * 2
print(new_word)