word_1 = input()
word_2 = input()

word_3 = list(word_1)

for char in range (len(word_1)):
    if word_1[char] != word_2[char]:
        word_3[char] = word_2[char]
        print("".join(word_3))