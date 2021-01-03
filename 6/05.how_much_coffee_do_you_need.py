line = input()
cofee = 0
list_of_activities = ["coding", "dog", "cat", "movie"]
while not line == "END":
    if line.lower() in list_of_activities:
        if line.islower():
            cofee += 1
        if line.isupper():
            cofee += 2
    line = input()

if cofee > 5:
    print("You need extra sleep")
else:
    print(cofee)