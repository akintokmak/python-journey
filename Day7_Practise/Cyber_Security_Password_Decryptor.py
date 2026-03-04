import random

from wordListDirectory import word_list


chosen_word = random.choice(word_list)
print(f"Word to guess: {chosen_word}")

lives = 6
print(f"Current Lives: {lives}")
game_over = False
correct_letters = []
while not game_over:
    guess_a_letter = input("Guess a letter: ").lower()

    if len(guess_a_letter) != 1 or not guess_a_letter.isalpha():
        print("Invalid input! Please enter only a single letter.")
    else:
        if guess_a_letter in correct_letters:
            print(f"You have already guessed this letter: {guess_a_letter}")
        display = []

        for letter in chosen_word:
            if guess_a_letter == letter:
                display.append(letter)
                correct_letters.append(letter)
            elif letter in correct_letters:
                display.append(letter)
            else:
                display.append("_")

        if guess_a_letter not in chosen_word:
            lives -= 1
            print(f"Access Denied! You lost a life. Remaining lives: {lives}")
            if lives == 0:
                print(f"System Locked! The word was: {chosen_word}")
                game_over = True
        print(f"Firewall Integrity: {'█' * lives}{'░' * (6 - lives)}")
        if '_' not in display:
            print("Access Granted!")
            game_over = True

        print(' '.join(display))



