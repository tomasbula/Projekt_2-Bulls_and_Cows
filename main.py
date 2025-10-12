import random
import time

number_length = 4  # Length of the number

def separator_1():      # Function for single separator line
    """Single separator line"""
    print("-" * 50)

def separator_2():      # Function for double separator line
    """Double separator line"""
    print("=" * 50)

def secret_number_generator():  # Function to generate a random number with unique digits
    """
    Generating a random number with unique digits
    
    Returns:
        int: Randomly generated number with unique digits
    """
    digits = list("0123456789")
    while True:
        number = random.sample(digits, number_length)
        if number[0] != '0':
            return int("".join(number))

def get_user_guess():   # Function to get user input
    """
    Getting and validating user input for a number with unique digits
    
    Returns:
        int: Validated number input by the user
    """
    while True:
        user_input = input(">>> ")
        # Empty input check
        if not user_input:
            print("Input cannot be empty.")
            separator_1()
            continue
        # Check if the number not starts with 0
        if user_input[0] == '0':
            print("Number must not start with 0.")
            separator_1()
            continue
        # Check if input contains only digits
        if not user_input.isdigit():                    
            print("Please enter digits only.")
            separator_1()
            continue
        # Digits length check
        if len(user_input) != number_length:
            print(f"Please enter a {number_length}-digit number.")
            separator_1()
            continue
        # Digits uniqueness check
        if len(set(user_input)) != number_length:
            print("Digits must be unique.")
            separator_1()
            continue
        return int(user_input)

def number_to_list(number): # Function to convert a number to a list of its digits
    """Convert a number to a list of its digits"""
    return [int(digit) for digit in str(number)]

def game_bulls_and_cows():      # Function for the main game starting and logic
    """
    Main function for the Bulls & Cows game.
    
    The player guesses a randomly generated 4-digit number with unique digits.
    After each attempt by the player, the number of "bulls" and "cows" is displayed
    The game continues until the player guesses the correct number.
    After guessing the number, the number of attempts and the total time of the game are displayed.
    """
    # Introduction of the game Bulls & Cows
    separator_2()
    print("Hi there!")
    separator_1()
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    separator_1()
    print("Enter a number:")
    separator_1()
    # Main game logic
    secret_number = secret_number_generator()   # Generating the secret number
    user_number = 0         # Default user number
    attempts = 0            # Attempts counter - default value
    
    start = time.time()  # Time measurement start   
    while True:
        attempts += 1   # Attempts counter increment
        user_number = get_user_guess()  # Getting user input
        secret_number_to_list = number_to_list(secret_number)   # Conversion of the secret number to a list
        user_number_to_list = number_to_list(user_number)       # Conversion of the user number to a list

        # To find indices where bulls are (same number in the same place)
        bull_indices = [i for i, (u, s) in enumerate(zip(user_number_to_list, secret_number_to_list)) if u == s]
        total_bulls = len(bull_indices)

        # To get remaining digits for cows (those that are not bulls)
        user_remaining = [u for i, u in enumerate(user_number_to_list) if i not in bull_indices]
        secret_remaining = [s for i, s in enumerate(secret_number_to_list) if i not in bull_indices]

        # To count cows (correct number, wrong place)
        total_cows = 0
        for u in user_remaining:
            if u in secret_remaining:
                total_cows += 1
                secret_remaining.remove(u)  # So as not to be counted more than once

        if total_bulls == 4:    # Statement when guessing the number correctly
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            separator_1()
            print("That's amazing!")
            separator_1()
            break         
        else:   # Bulls & cows listing with respect to singular/plural
            bull_word = "bull" if total_bulls == 1 else "bulls"
            cow_word = "cow" if total_cows == 1 else "cows"
            print(f"{total_bulls} {bull_word}, {total_cows} {cow_word}")
            separator_1()   
    end = time.time()  # Measurement end time
    
    # Total game time
    total_time = end - start
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)   
    print(f"Total time: {minutes} min. and {seconds} sec.")
    separator_1()

def repeat_the_game():      # Function to repeat the game
    """
    Function to repeat the Bulls & Cows game.
    
    After finishing one game, the user is asked if he wants to play again:
    "yes" => the game restarts / "no" => the program exits with thanks.
    """
    while True:
        game_bulls_and_cows()
        # Game repetition question with input validation
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        separator_1()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    repeat_the_game()
