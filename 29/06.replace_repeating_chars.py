data = input()
new_data = data[0]
for i in range(1, len(data)):
    if data[i] == data[i-1]:
        continue
    else:
        new_data += data[i]

print(new_data)
# command = "aaaaabbbbbcdddeeeedssaa"
# i = 0
#
# while i < len(command) - 1:
#     if command[i] == command[i+1]:
#         command = command.replace(command[i], "")
#         i = 0
#     else:
#         i += 1
#
# print(command)