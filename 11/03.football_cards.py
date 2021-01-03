team_a_players_count = 11
team_b_players_count = 11

team_a_players_with_red_cards = []
team_b_players_with_red_cards = []

input_line = input()
input_line = input_line.split()

is_terminated = False

for i in input_line:
    if i in team_a_players_with_red_cards or i in team_b_players_with_red_cards:
        continue

    if i[0] == "A":
        team_a_players_count -= 1
        team_a_players_with_red_cards.append(i)
    else:
        team_b_players_count -= 1
        team_b_players_with_red_cards.append(i)

    if team_a_players_count < 7 or team_b_players_count < 7:
        is_terminated = True
        break


print(f"Team A - {team_a_players_count}; Team B - {team_b_players_count}")

if is_terminated:
    print(f"Game was terminated")

# Second_solution


received_cards = input()

cards_list = received_cards.split()
A_cards = []
B_cards = []

A_team = 11
B_team = 11

is_terminated = False

for item in range(len(cards_list)):
    if cards_list[item][0] == "A":
        if cards_list[item] in A_cards:
            pass
        else:
            A_cards.append(cards_list[item])
            A_team -= 1

    if cards_list[item][0] == "B":
        if cards_list[item] in B_cards:
            pass
        else:
            B_cards.append(cards_list[item])
            B_team -= 1

    if A_team < 7 or B_team < 7:
        is_terminated = True
        break

print(f"Team A - {A_team}; Team B - {B_team}")
if is_terminated:
    print(f"Game was terminated")