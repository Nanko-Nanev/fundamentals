ban_list = input().split(", ")
text_to_format = input()

for word in ban_list:
    while word in text_to_format:
        text_to_format = text_to_format.replace(word, "*" * (len(word)))

print(text_to_format)