energy = 100
coins = 100
flag = True

line = input().split("|")

for el in line:
    event, number = el.split("-")
    number = int(number)

    if event == "rest":
        gained_energy = 0
        if number + energy <= 100:
            energy += number
            gained_energy = number
        else:
            gained_energy = 0
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")

        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins > number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            flag = False
            break


if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")