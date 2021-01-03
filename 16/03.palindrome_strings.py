words = input().split()
searched_palindrome = input()
found_palindrome_counter = 0
result = []

for word in words:
    if word == word[::-1]:
        result.append(word)

print(result)

for word in result:
    if word == searched_palindrome:
        found_palindrome_counter += 1

print(f"Found palindrome {found_palindrome_counter} times")