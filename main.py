import random
import time


# Length of the number
number_length = 4

# Length of the separator lines
separator_length = 50


def separator_1():
    
    """Single separator line"""
    
    print("-" * separator_length)


def separator_2():
    
    """Double separator line"""
    
    print("=" * separator_length)


def secret_number_generator():
   
    """
    Generating a random number with unique digits
    
    Returns:
        int: Randomly generated number with unique digits
    """
   
    digits = list("0123456789")
   
    while True:
     
        number = random.sample(digits, number_length)
    
        # Ensure the first digit is not '0' to avoid leading zeros
        if number[0] != '0':
            return int("".join(number))


def get_user_guess():
    
    """
    Getting and validating user input for a number with unique digits
    
    Returns:
        int: Validated number input by the user
    
    """
    while True:
        
        user_input = input(">>> ")

        error_message = None
        
        # Empty input check
        if not user_input:
            error_message = "Input cannot be empty."
        
        # Check if the number not starts with 0
        elif user_input[0] == '0':
            error_message = "Number must not start with 0."
        
        # Check if input contains only digits
        elif not user_input.isdigit():
            error_message = "Please enter digits only."
        
        # Digits length check
        elif len(user_input) != number_length:
            error_message = f"Please enter a {number_length}-digit number."
        
        # Digits uniqueness check
        elif len(set(user_input)) != len(user_input):
            error_message = "Digits must be unique."
        
        if error_message:
            print(error_message)
            separator_1()
            continue

        return int(user_input)


def number_to_list(number):
    
    """Convert a number to a list of its digits"""
    
    return [int(digit) for digit in str(number)]


def game_bulls_and_cows():
    
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
    
    # Generating the secret number
    secret_number = secret_number_generator()
    
    # Default user number
    user_number = 0   

    # Attempts counter - default value
    attempts = 0
    
    # Time measurement start 
    start = time.time()   
    
    while True:

        # Attempts counter increment
        attempts += 1   
        user_number = get_user_guess()
        secret_number_to_list = number_to_list(secret_number)
        user_number_to_list = number_to_list(user_number)

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
                secret_remaining.remove(u)

        # Statement when guessing the number correctly
        if total_bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            separator_1()
            print("That's amazing!")
            separator_1()
            break         
        
        # Bulls & cows listing with respect to singular/plural
        else:
            bull_word = "bull" if total_bulls == 1 else "bulls"
            cow_word = "cow" if total_cows == 1 else "cows"
            print(f"{total_bulls} {bull_word}, {total_cows} {cow_word}")
            separator_1()   
    
    # Measurement end time
    end = time.time()
    
    # Total game time
    total_time = end - start
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)   
    
    print(f"Total time: {minutes} min. and {seconds} sec.")
    separator_1()


def repeat_the_game():
    
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
