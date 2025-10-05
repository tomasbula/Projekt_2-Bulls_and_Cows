import random
import time

def separator_1():      # Funkce pro oddělovací čáru
    """Oddělovací čára"""
    print("-" * 50)

def separator_2():      # Funkce pro dvojitou oddělovací čáru
    """Dvojitá oddělovací čára"""
    print("=" * 50)

def secret_number_generator():  # Funkce pro generování náhodného 4-místného čísla
    """
    Generování náhodného 4-místného čísla s unikátními číslicemi
    
    Returns:
        int: Náhodně vygenerované 4-místné číslo
    """
    while True:
        generated_number = random.randint(1000, 9999)
        digits = str(generated_number)
        if len(set(digits)) == 4:  # kontrola unikátnosti číslic
            break
    return generated_number

def get_user_guess():   # Funkce pro číslo zadané uživatelem
    """
    Získání a validace čísla zadaného uživatelem
    
    Returns:
        int: Validované 4-místné číslo zadané uživatelem
    """
    while True:
        user_input = input(">>> ")
        # Kontrola, zda zadané číslo nezačíná nulou
        if user_input[0] == '0':
            print("Number must not start with 0.")
            separator_1()
            continue
        # Kontrola, zda jsou zadány pouze číslice
        if not user_input.isdigit():                    
            print("Please enter digits only.")
            separator_1()
            continue
        # Kontrola délky zadaného čísla (pouze 4 číslice)
        if len(user_input) != 4:
            print("Please enter a 4-digit number.")
            separator_1()
            continue
        # Kontrola unikátnosti číslic
        if len(set(user_input)) != 4:
            print("Digits must be unique.")
            separator_1()
            continue
        return int(user_input)

def number_to_list(number): # Funkce pro převod čísla na list číslic
    """Převod 4-místných čísel na listy číslic"""
    return [int(digit) for digit in str(number)]

def game_bulls_and_cows():      # Funkce pro spuštění hry
    """
    Hlavní funkce pro hru Bulls & Cows
    
    Hráč hádá náhodně vygenerované 4-místné číslo s unikátními číslicemi.
    Po každém pokusu hráče se vypíše počet "bulls" a "cows"
    Hra pokračuje, dokud hráč neuhodne správné číslo.
    Po uhodnutí čísla se vypíše počet pokusů a celkový čas hry.
    """
    # Úvod a představení hry Bulls & Cows
    separator_2()
    print("Hi there!")
    separator_1()
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    separator_1()
    print("Enter a number:")
    separator_1()
    # Hlavní program hry
    secret_number = secret_number_generator()   # Generování tajného čísla
    user_number = 0         # Výchozí hodnota pro uživatelské číslo
    attempts = 0            # Počet pokusů uživatele - výchozí hodnota
    
    start = time.time()  # Start měření času   
    while True:
        attempts += 1   # Počítadlo pokusů
        user_number = get_user_guess()  # Získání čísla od uživatele
        secret_number_to_list = number_to_list(secret_number)   # Převod tajného čísla na list
        user_number_to_list = number_to_list(user_number)       # Převod uživatelského čísla na listc
        total_bulls = 0     # Celkový počet bulls - výchozí hodnota
        total_cows = 0      # Celkový počet cows - výchozí hodnota
        # Pomocné seznamy pro pozice, které už byly použity
        bulls_indices = []
        cows_indices_secret = []
        cows_indices_user = []

        for i in range(4):      # Hledání bulls a jejich pozic
            if user_number_to_list[i] == secret_number_to_list[i]:
                total_bulls += 1
                bulls_indices.append(i)

        for i in range(4):      # Hledání cows s ohledem na již nalezené bulls
            if i in bulls_indices:
                continue  # Přeskoč bulls

            for j in range(4):
                if j in bulls_indices or j in cows_indices_secret:
                    continue  # Nepoužívej pozice označené jako bulls nebo použité pro jinou cow
                if user_number_to_list[i] == secret_number_to_list[j]:
                    total_cows += 1
                    cows_indices_secret.append(j)
                    cows_indices_user.append(i)
                    break
        
        if total_bulls == 4:    # Výpis při správném uhodnutí čísla
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            separator_1()
            print("That's amazing!")
            separator_1()
            break         
        else:   # Výpis bulls & cows s ohledem na jednotné/množné číslo
            bull_word = "bull" if total_bulls == 1 else "bulls"
            cow_word = "cow" if total_cows == 1 else "cows"
            print(f"{total_bulls} {bull_word}, {total_cows} {cow_word}")
            separator_1()   
    end = time.time()  # Konec měření času
    
    # Celkový čas hry
    total_time = end - start
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)   
    print(f"Total time: {minutes} min. and {seconds} sec.")
    separator_1()

def repeat_the_game():      # Funkce pro opakování hry
    """
    Funkce pro opakování hry Bulls & Cows
    
    Po skončení jedné hry se uživatele zeptá, zda chce hrát znovu:
    "yes" => hra se restartuje / "no" => program se ukončí s poděkováním.
    """
    while True:
        game_bulls_and_cows()
        # Dotaz na opakování hry s ošetřením na velká/malá písmena a odstranění mezer
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        separator_1()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break

repeat_the_game()