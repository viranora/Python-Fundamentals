"""
Python Fundamentals - Mini Project: Number Guessing Game
Description: A game where the computer picks a random number between 1 and 100,
and the user tries to guess it with hints (Too High / Too Low).
"""

import random # Importing the random module to generate numbers

def start_game():
    print("==================================")
    print("  WELCOME TO THE GUESSING GAME  ")
    print("==================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    # 1. Computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = 0 

    # 2. The Loop runs until the user guesses correctly
    while guess != secret_number:
        try:
            # Get input and convert to integer
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1 # Increment attempt counter

            # 3. Decision Logic
            if guess < secret_number:
                print(">> Too Low! Try higher. ⬆️")
            elif guess > secret_number:
                print(">> Too High! Try lower. ⬇️")
            else:
                print(f"\n🎉 CONGRATULATIONS! You found it!")
                print(f"The number was {secret_number}.")
                print(f"It took you {attempts} attempts.")
        
        except ValueError:
            # Handle case where user enters text instead of number
            print("⚠️ Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    start_game()