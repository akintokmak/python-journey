from art import logo , vs_art
from game_data import data
import random


def format_name(account) -> str:
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name} a {account_description} from {account_country}"

def get_winner(count_a, count_b) -> str:
    if count_a > count_b:
        return 'a'
    elif count_b > count_a:
        return 'b'
    return 'tie'

def is_correct(user_guess,winner) -> bool:
    return user_guess == winner

def get_user_guess() -> str:
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        if guess in ('a', 'b'):
            return guess
        print("Invalid input! Please type 'A' or 'B'.")

def game():
    print(logo)
    score = 0

    account_b = random.choice(data)
    while True:

        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_name(account_a)}")
        print(vs_art)
        print(f"Against B: {format_name(account_b)}")

        user_guess = get_user_guess()

        print("\n" * 20)
        print(logo)
        account_follower_count_A = account_a["follower_count"]
        account_follower_count_B = account_b["follower_count"]
        winner = get_winner(count_a=account_follower_count_A,count_b=account_follower_count_B)
        compare = is_correct(user_guess,winner)

        if compare:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score:{score}")
            break

game()




