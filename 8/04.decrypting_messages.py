key = int(input())
number_of_lines = int(input())
result = ""

for i in range(number_of_lines):
    a = chr(ord(input()) + key)
    result += a

print(result)