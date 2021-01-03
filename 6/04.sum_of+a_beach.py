line = input().lower()

searched_words = ["sand", "water", "fish", "sun"]
counter = 0

for i in range(len(searched_words)):
    counter += line.count(searched_words[i])

print(counter)