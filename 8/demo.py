n = int(input())
right = 0
left = 0
opening = 0
for i in range(1, n + 1):
    sigh = input()
    if sigh == '(':
        opening += 1
        left += 1
    if sigh == ')':
        right += 1
        opening = 0

    if opening == 2:
        break

if left == right:
    print("BALANCED")
else:
    print("UNBALANCED")