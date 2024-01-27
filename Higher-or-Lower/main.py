from art import logo
from game_data import data
import random

print(logo)

PLAYER_POINTS = 0

still_going = True

first_random = random.choice(data)
second_random = random.choice(data)

desired_keys = ["name", "description", "country"]

remaining = first_random

while still_going:
    if remaining == second_random:
        second_random = random.choice(data)

    for key in desired_keys:
        value = remaining.get(key)
        print(f"    {key}: {value}")
    print("\n & \n")

    for key in desired_keys:
        value = second_random.get(key)
        print(f"    {key}: {value}")
    print("\n\n")

    guess = input("who has the most follower? A or B?: ").lower()
    print("\n")
    answer = ""

    if int(remaining.get("follower_count")) > int(second_random.get("follower_count")):
        answer = "a"
        second_random = random.choice(data)

    elif int(remaining.get("follower_count")) < int(
        second_random.get("follower_count")
    ):
        answer = "b"
        remaining = second_random
        second_random = random.choice(data)

    if guess == answer:
        print("Correct!")
        print("\nNEXT ONE:\n")
        PLAYER_POINTS += 1
    else:
        print(f"\nGAME OVER! You got {PLAYER_POINTS} points")
        still_going = False
