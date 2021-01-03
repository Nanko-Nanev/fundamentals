party_size = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):

    if i % 15 == 0:
        party_size += 5

    if i % 10 == 0:
        party_size -= 2

    coins += 50
    coins -= 2 * party_size

    if i % 3 == 0:
        coins -= 3 * party_size

    if i % 5 == 0:
        coins += 20 * party_size
        if i % 3 == 0:
            coins -= 2 * party_size

coins_per_person = coins / party_size

print(f"{party_size} companions received {int(coins_per_person)} coins each.")