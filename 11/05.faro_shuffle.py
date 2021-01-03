cards = input().split()
number = int(input())

start_card = cards[0]
end_card = cards[-1]
cards.pop(0)
cards.pop()

shuffled_cards = []
first_half = []
second_half = []
before_shuffle = cards.copy()
half_size = int(len(cards) / 2)

for j in range(number):

    for i in range(half_size):
        first_half.append(before_shuffle[i])
    for i in range(half_size, len(cards)):
        second_half.append(before_shuffle[i])
    shuffled_cards = []
    for i in range(half_size):
        shuffled_cards.append(second_half[i])
        shuffled_cards.append(first_half[i])

    first_half = []
    second_half = []
    before_shuffle = shuffled_cards.copy()


shuffled_cards.append(end_card)
shuffled_cards.insert(0,start_card)

print(shuffled_cards)