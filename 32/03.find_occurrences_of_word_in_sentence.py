import re
line = input().lower()
find_word = input().lower()
# find_word_2 = fr"{find_word}(?=\s)*"
pattern = fr"\b{find_word}\b"

match = re.findall(pattern, line)

print(len(match))

