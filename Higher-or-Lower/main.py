from art import logo
from game_data import data
import random

print(logo)

PLAYER_POINTS = 0

still_going = True

first_random = random.choice(data)

desired_keys = ["name", "description", "country"]

for key in desired_keys:
    value = first_random.get(key)
    print(f"    {key}: {value}")

second_random = random.choice(data)
for key in desired_keys:
    value = second_random.get(key)
    print(f"    {key}: {value}")

# while still_going:
#     print(remaining)
#     newer = print(random.choice(data).key[0, 2, 3])
#     guess = print("who has the most follower? A or B?")
#     print(remaining.key[0, 2, 3])
#     print(newer.key[0, 2, 3])
#     if remaining.key[1] > newer.key[1]:
#         answer = "A"
#     elif first_random.key[1] < newer.key[1]:
#         answer = "B"
#         remaining = newer
#     if guess == answer:
#         print("correct")
