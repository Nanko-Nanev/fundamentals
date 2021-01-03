string = input().split()
n = int(input())

string = [int(i) for i in string]

for i in range(n):
    string.remove(min(string))
print(string)