def free_chair_from_room(available, taken):
    free_chairs_to_add = 0
    chairs_count = len(available)
    taken_chairs = int(taken)
    free_chairs_to_add += (chairs_count - taken_chairs)
    return free_chairs_to_add


n_rooms = int(input())
free_chairs = 0
no_print = True

for i in range(1, n_rooms+1):
    command = input().split()
    free_chairs += free_chair_from_room(command[0], command[1])
    if free_chair_from_room(command[0], command[1]) < 0:
        print(f"{free_chair_from_room(command[0], command[1]) * -1} more chairs needed in room {i}")
        no_print = False

if no_print:
    print(f"Game On, {free_chairs} free chairs left")
