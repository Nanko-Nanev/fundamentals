message = input().split()
new_message = []

for word in message:
    word_to_convert = ""
    word_result = []
    for i in range(len(word)):
        if word[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            word_to_convert += word[i]
        else:
            word_result.append(word[i])
    word_to_convert = chr(int(word_to_convert))
    word_result[0], word_result[len(word_result)-1] = word_result[len(word_result)-1], word_result[0]
    word_result = word_to_convert + "".join(word_result)
    new_message.append(word_result)

new_message = " ".join(new_message)
print(new_message)