num = input()
char_num = str(num)
num_list = []

for char in char_num:
    num_list += [char]

for i in range(len(str(num))):
    print(max(num_list), end="")
    num_list.remove(max(num_list))

