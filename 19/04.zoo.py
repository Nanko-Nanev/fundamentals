class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.births = []

    def add_animals(self, species, names):
        if species == "mammal":
            self.mammals.append(names)
        elif species == "fish":
            self.fishes.append(names)
        elif species == "bird":
            self.births.append(names)
        Zoo.__animals += 1

    def get_info(self, info):
        result = ''
        if info == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif info == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif info == "bird":
            result = f"Birds in {self.name}: {', '.join(self.births)}\n"
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for i in range(number):
    line = input()
    species, name = line.split()
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammals":
#             self.mammals.append(name)
#         elif species == "fishes":
#             self.fishes.append(name)
#         elif species == "birds":
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammals":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)} \n"
#         elif species == "fishes":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)} \n"
#         elif species == "birds":
#             result += f"Birds in {self.name}: {', '.join(self.birds)} \n"
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# n = int(input())
#
# for i in range(n):
#     command = input().split(" ")
#     Zoo.add_animal(command[0], command[1])
#
# info_for_species = input()
# print(Zoo.get_info(info_for_species))

