from art import logo
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
NUMBER_RANGE = (1, 100)




def generate_number() -> int:
    return random.randint(*NUMBER_RANGE)


def set_difficulty() -> int:
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def check_guess(guess: int, answer: int) -> str:

    if guess > answer:
        return "high"
    elif guess < answer:
        return "low"
    return "correct"


def get_user_guess() -> int:
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")



def game() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {NUMBER_RANGE[0]} and {NUMBER_RANGE[1]}.")

    secret_number = generate_number()
    turns_remaining = set_difficulty()

    while turns_remaining > 0:
        print(f"\nYou have {turns_remaining} attempt(s) remaining.")
        user_guess = get_user_guess()
        result = check_guess(user_guess, secret_number)

        if result == "correct":
            print(f"🎉 You got it! The answer was {secret_number}.")
            return

        turns_remaining -= 1

        if result == "high":
            print("Too high!")
        else:
            print("Too low!")

        if turns_remaining > 0:
            print("Guess again.")

    print(f"\n💀 You ran out of attempts! The number was {secret_number}.")


if __name__ == "__main__":
    game()