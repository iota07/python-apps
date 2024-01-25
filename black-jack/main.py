from art import logo
from rules import rules
import random

print(logo)
print(rules)

should_end = False
cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,

}


game_continue = input(f'Would you like to play? "y" for Yes, "n" for No: \n').lower()
if game_continue == "n":
    should_end = True
    print("Goodbye!")

player_cards = {}
computer_cards = {}

def add_random_card_to_dict(source_dict, target_dict):
    # Get a random key from the source_dict
    random_key = random.choice(list(source_dict.keys()))
    
    # Add the key-value pair to the target_dict
    target_dict[random_key] = source_dict[random_key]

while not should_end:
    player_cards = {}
    add_random_card_to_dict(cards, player_cards)
    add_random_card_to_dict(cards, player_cards)
    print("Here are your cards:", list(player_cards.keys()))
    player_sum = sum(player_cards.values())
    computer_cards = {}
    add_random_card_to_dict(cards, computer_cards)
    add_random_card_to_dict(cards, computer_cards)
    print("The dealer opened card is: ", list(computer_cards.keys())[0] + ', X')
    computer_sum = sum(computer_cards.values())
    
    # Propose player a card
    player_want_card = True
    while player_want_card:

        if (input(f"Would you like another card? type 'y' for Yes or type 'n' for No: ").lower() == "y"):
            add_random_card_to_dict(cards, player_cards)
            print("Here are your cards:", list(player_cards.keys()))
            player_sum = sum(player_cards.values())
                          
            if player_sum > 21:
                if "A" in player_cards:
                    player_cards["A"] = 1
                    player_sum = sum(player_cards.values())
                    if player_sum > 21:
                        player_want_card = False
                        print("Busted! your cards total value is", player_sum)
                        print("GAME OVER!")
                        
                else:
                    player_want_card = False
                    print("Busted! your cards total value is", player_sum)
                    print("GAME OVER!")
        else:
            player_want_card = False
    
    if player_sum < 22:
        print("Dealer reveal his second card:", list(computer_cards.keys()))

        computer_draw_card = True
        while computer_draw_card:
            print("Dealer's cards:", list(computer_cards.keys()))
            if computer_sum < 16:
                add_random_card_to_dict(cards, computer_cards)
                print("Dealer hit a card:", list(computer_cards.keys()))
                computer_sum = sum(computer_cards.values())
                if computer_sum > 21:
                    if "A" in computer_cards:
                        computer_cards["A"] = 1
                        computer_sum = sum(computer_cards.values())
                        if computer_sum > 21:
                            computer_draw_card = False
                            print("Busted! dealer's card total value is", player_sum)
                            print("GAME OVER! You Win!")
                        elif computer_sum <= 21:
                            computer_draw_card = False
            else:
                computer_draw_card = False

        if computer_sum <= player_sum and computer_sum < 20:
            add_random_card_to_dict(cards, computer_cards)
            print("Dealer hit a new card:", list(computer_cards.keys()))
            if computer_sum > 21:
                computer_draw_card = False
                print("Busted! dealer's card total value is", player_sum)
                print("GAME OVER! You Win!")
        if player_sum == 21:
            print("GAME OVER! You Win!")
        elif player_sum == 20:
            if computer_sum == 21:
                print("GAME OVER! Bank Win!")
            if computer_sum == 20:
                print("Player lose, house bonus+1, Bank win!")
    else:
        print("Busted! your cards total value is", player_sum)
        print("GAME OVER!")
    

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Thanks for playing Black Jack! Goodbye!")


    


