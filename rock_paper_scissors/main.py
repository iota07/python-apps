import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choice = input("What is your choice? Rock, Paper or Scissors?\n")
player_choice = player_choice.lower()

if player_choice == "rock":
    print(f"Your choice is:{rock}")
elif player_choice == "paper":
    print(f"Your choice is:{paper}")
elif player_choice == "scissors":
    print(f"Your choice is:{scissors}")
else:
    print("Your choice is: Invalid. You lose !\n")


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"Computer choice is: {rock}")
elif computer_choice == 1:
    print(f"Computer choice is: {paper}")
else:
    print(f"Computer choice is: {scissors}")

if player_choice == "rock" and computer_choice == 1:
    print("You lose !")
elif player_choice == "rock" and computer_choice == 0:
    print("Draw")
elif player_choice == "rock" and computer_choice == 2:
    print("You win !")

if player_choice == "paper" and computer_choice == 2:
    print("You lose !")
elif player_choice == "paper" and computer_choice == 1:
    print("Draw")
elif player_choice == "paper" and computer_choice == 0:
    print("You win !")

if player_choice == "scissors" and computer_choice == 0:
    print("You lose !")
elif player_choice == "scissors" and computer_choice == 2:
    print("Draw")
elif player_choice == "scissors" and computer_choice == 1:
    print("You win !")
