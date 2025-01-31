import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls')

clear_screen()
chosen_word = random.choice(word_list)
# print(chosen_word)
print(logo)
placeholder = " "
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)
lives = 6
correct_letters = []
wrong_guesses = []
game_over = False
while not game_over:
    display = ""
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in wrong_guesses:
        print(f"you've already guessed {guess}!")
    elif guess not in chosen_word:
        wrong_guesses.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Now you have {lives} lives!")
        if lives == 0:
            print("you lose!")
            print(f"The word was '{chosen_word}'!")
            # break
            game_over = True
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_ '
    if "_" not in display:
        game_over = True
        print("you win!")
        print(f"The word was '{chosen_word}'!")
    print(display)
    print(stages[lives])
