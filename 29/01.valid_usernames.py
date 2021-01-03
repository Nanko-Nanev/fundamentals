names = input().split(", ")

for name in names:
    if 3 <= len(name) <= 16 and (name.isalnum() or '_' in name or '-' in name):
        print(name)

# command = input().split(", ")
# result = []
#
# for user in command:
#     if 3 < len(user) < 16:
#         result.append(user)
#
#
# for user in result:
#     if " " in user or "@" in user or "!" in user:
#         result.remove(user)
#
# for user in result:
#     if user.isalpha() and user.isdigit():
#         result.remove(user)
#
# for user in result:
#     print(f"{user}")