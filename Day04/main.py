import random
import os

# Define the game choices as a list for easy access
choices = [
'''rock : 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''paper :
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''scissors :
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
]

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls')

# Start the game loop
while True:

    # Clear the screen at the start of each round
    clear_screen()

    # Get user input
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.Type 3 to exit.\n"))
        if user_choice == 3:
            print("Thanks for playing! Goodbye!")
            break

        # Validate input
        if user_choice not in [0, 1, 2]:
            print("Invalid choice. Please select 0, 1, or 2.")
            input("Press Enter to continue...")
            continue #The 'continue' statement skips the rest of the code in the loop for that iteration and jumps back to the start of the loop, prompting the user for input again.
        
        # Print user choice
        print(f"You chose:\n{choices[user_choice]}")
        print("\n")
        # Print computer choice
        computer_choice = random.randint(0, 2) #randint(a, b) function:This function generates a random integer between a and b (inclusive). In this case, it will generate a number between 0 and 3, including both endpoints (0, 1, or 2).
        print(f"Computer chose:\n{choices[computer_choice]}")

        # Determine the result
        if user_choice == computer_choice:
            print("It's a draw!")

        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("you win!")
        else:
            print("you lose!")

        # Pause before clearing the screen for the next round
        input("Press Enter to continue...")

    except ValueError: #it is not strictly necessary to specify the type of error after 'except'. If you omit it, the except block will catch all exceptions, regardless of their type.
        print("Invalid input! Please enter a number between 0 and 3.")
        input("Press Enter to continue...") #After this line is executed, the program waits for the user to press the Enter key. Once the user presses Enter: The program resumes execution from where it left off, which in this case means the loop will restart (if it is inside a loop).


