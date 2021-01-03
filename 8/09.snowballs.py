snowballs = int(input())
snowball_value = []
top_snowball_snow = 0
top_snowball_time = 0
top_snowball_quality = 0
top_snowball_value = 0

for i in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value.append((snowball_snow / snowball_time) ** snowball_quality)
    if snowball_value[-1] == max(snowball_value):
        top_snowball_snow = snowball_snow
        top_snowball_time = snowball_time
        top_snowball_quality = snowball_quality
        top_snowball_value = snowball_value[-1]

print(f"{top_snowball_snow} : {top_snowball_time} = {int(top_snowball_value)} ({top_snowball_quality})")