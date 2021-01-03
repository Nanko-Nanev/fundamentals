line = input().split(", ")
counter = 0
if line[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for word in line[::-1]:

        if word == "wolf":
            print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
            break
        counter += 1
