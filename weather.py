import random

day = int(input('How many days of the forcast do you want?: '))

for i in range(1, day + 1):
    temp = random.randint (60, 86)
    rain = random.randint (0, 50)
    print(f'Day {i}: Temperature = {temp}°F -- Precipitation Chance = {rain}%')
