from art import logo
import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.add(1)
    return sum(cards)


def compare(user_scores, computer_scores):
    """Compares the user score u_score against the computer score c_score."""
    if user_scores == computer_scores:
        print("It's a draw.")
    elif computer_scores == 0:
        print("You lose, opponent has Blackjack.")
    elif user_scores == 0:
        print("Win with a Blackjack.")
    elif user_scores > 21:
        print("You went over, you lose.")
    elif computer_scores > 21:
        print("Opponent went over, you win.")
    elif user_scores > computer_scores:
        print("You win.")
    else:
        print("You lose.")


def play_game():
    print(logo)
    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1
    game_is_not_over = False

    for _ in range(2):
        user_card.append(deal_card())
    computer_card.append(deal_card())

    while not game_is_not_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current_score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_not_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                game_is_not_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_scores=user_score, computer_scores=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()













