friends = input().split(", ")
commands = input().split()
blacklisted_names_count = 0
lost_names_count = 0

while not commands[0] == "Report":
    if commands[0] == "Blacklist":
        if commands[1] in friends:
            print(f"{commands[1]} was blacklisted.")
            loc = friends.index(commands[1])
            friends[loc] = "Blacklisted"
            blacklisted_names_count += 1
        else:
            print(f"{commands[1]} was not found.")

    elif commands[0] == "Error":
        if friends[int(commands[1])] == "Blacklisted" or friends[int(commands[1])] == "Lost":
            pass
        else:
            print(f"{friends[int(commands[1])]} was lost due to an error.")
            lost_names_count += 1
            friends[int(commands[1])] = "Lost"

    elif commands[0] == "Change":
        if 0 < int(commands[1]) <= len(friends) - 1:
            if commands[2] != friends[int(commands[1])]:
                print(f"{friends[int(commands[1])]} changed his username to {commands[2]}.")
                friends[int(commands[1])] = commands[2]

    commands = input().split()

print(f"Blacklisted names: {blacklisted_names_count}")
print(f"Lost names: {lost_names_count}")

for name in friends:
    print(f"{name}", end=" ")