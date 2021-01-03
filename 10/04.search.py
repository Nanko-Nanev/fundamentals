n = int(input())
special_world = input()
list_of_all_words = []
list_of_special_words = []

for i in range(n):
    new_word = input()
    list_of_all_words.append(new_word)
    if special_world in new_word:
        list_of_special_words.append(new_word)

print(list_of_all_words)
print(list_of_special_words)