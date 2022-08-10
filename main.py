# Black Jack Project
import random
from replit import clear
from art import logo


def deal_card():
    # returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        print("Black Jack!")
        score = 0
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score -= 10
    return score


def computer_plays(cards, computer_score, user_score):
    if computer_score == 0:
        computer_score = 21
    if user_score == 0:
        user_score = 21

    if user_score == computer_score and computer_score == 21:
        return 21
    if user_score >= computer_score and computer_score <= 16:
        while computer_score <= 16:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    return computer_score


flag = True
print(logo)
while (flag):
    inner_flag = True
    play = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
    clear()
    if play == 'y':
        user_cards = []
        computer_cards = []
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        while inner_flag:
            user_score = calculate_score(user_cards)
            print(
                f"    Your cards : {user_cards}, Current Score = {user_score}")
            print(f"    Computer's first card : {computer_cards[0]}")
            computer_score = calculate_score(computer_cards)
            if user_score > 21:
                print(
                    f"    Your final hand: {user_cards}, Your final score = {user_score}"
                )
                print(
                    f"    Computer's final hand : {computer_cards}, Computer's final score = {computer_score}"
                )
                print("    You lose! :( ")
                inner_flag = False

            elif user_score == 0:
                computer_score = computer_plays(computer_cards, computer_score,
                                                user_score)
                print(
                    f"    Your final hand: {user_cards}, Your final score = {user_score}"
                )
                print(
                    f"    Computer's final hand : {computer_cards}, Computer's final score = {computer_score}"
                )
                if computer_score == 21:
                    print("    Oops! Game resulted in a DRAW!")
                else:
                    print("    Congratulations! You won!")
                inner_flag = False

            else:
                end = input(
                    "Do you want to draw another card? Type 'y' for yes and 'n' for stand: "
                )
                if end == 'y':
                    user_cards.append(deal_card())
                    inner_flag = True
                else:
                    print(
                        f"    Your final hand: {user_cards}, Your final score = {user_score}"
                    )
                    computer_score = computer_plays(computer_cards,
                                                    computer_score, user_score)
                    print(
                        f"    Computer's final hand : {computer_cards}, Computer's final score = {computer_score}"
                    )
                    if computer_score == user_score:
                        print("    Oops! Game resulted in a DRAW!")
                    elif computer_score > user_score:
                        if computer_score <= 21:
                            print("    You lose! Sorry!")
                        else:
                            print("    Congratulations! You won!")
                    else:
                        print("    Congratulations! You won!")
                    inner_flag = False

    else:
        print("You chose to not play. See you later!")
        flag = False
