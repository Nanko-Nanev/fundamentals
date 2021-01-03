char_start = int(input())
char_stop = int(input())

for i in range(char_start, char_stop + 1):
    print(f"{chr(i)}", end=" ")