def add(username):
    if username in users_and_emails:
        print(f"{username} is already registered")
    else:
        users_and_emails[username] = []


def send(username, email):
    if username not in users_and_emails:
        users_and_emails[username] = email
    else:
        users_and_emails[username].append(email)


def delete(username):
    if username not in users_and_emails:
        print(f"{username} not found!")
    else:
        users_and_emails.pop(username)


data = input()
users_and_emails = {}

while not data == "Statistics":
    data = data.split("->")
    if data[0] == "Add":
        add(data[1])
    elif data[0] == "Send":
        send(data[1], data[2])
    elif data[0] == "Delete":
        delete(data[1])

    data = input()

print(f"Users count: {len(users_and_emails)}")
for user in sorted(users_and_emails):
    print(f"{user}")
    for mail in users_and_emails[user]:
        print(f" - {mail}")