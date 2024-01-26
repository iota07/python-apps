import random
from art import logo

print(logo)
print("\nWelcome to the Number Guessing Game\n")
print("I'm thinking of a number between 1 and 100\n")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


number_list = []
for number in range(1, 101):
    number_list.append(number)

selected_number = int(random.choice(number_list))

ATTEMPTS = set_difficulty()
still_going = True
while still_going:
    print(f"You have {ATTEMPTS} remaining to guess the number. What is your guess?\n")
    player_number = int(input())
    ATTEMPTS -= 1
    if ATTEMPTS == 0:
        still_going = False
        print("GAME OVER. No more attempts")

    elif player_number > selected_number:
        print("\nToo high\n")
    elif player_number < selected_number:
        print("\nToo low\n")

    elif player_number == selected_number:
        print(f"\nThe number I thought of was {selected_number}. You guessed right!\n")
        still_going = False

    else:
        print("Invalid guess")

print("Thank for playing")
