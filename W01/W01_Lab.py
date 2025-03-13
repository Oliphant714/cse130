# 1. Name
#     Isaac Oliphant
# 2. Assignment Name
#     Lab 01: Guessing Game
# 3. Assignment Description
#     The game takes a maximum integer from the user and picks a random integer between 1 and the user input.  It then asks the user to guess what the chosen integer is and informs the user if their guess is too high or low, after which it allows them to choose again.  The game ends when the user correctly guesses the integer at which point the game will display their guesses and number of attempts (if it was more than one) and gives the user the option to continue playing.  If the user decides to keep playing, it will loop back to the beginning.  If any other input is detected, the game will end.
# 4. What was the hardest part?
#     The hardest part was simply remembering the syntax; remembering to use list.append(variable) and variable.upper()  My main bug was the {attempt} variable and forgetting to have it updating inside the loop.  Once I solved that bug, the rest of the code was quite simple.
# 5. How long did it take you to complete the assignment?
#     It took me about a half hour, maybe a little more.

import random

print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')

keep_playing = "balderdash"

while keep_playing != "N":
    maximum = int(input("Pick a positive integer: "))
    correct_number = random.randint(1, maximum)

    print(f"Got it!  Please guess a positive integer between 1 and {maximum}:")
    guess = int(input(""))
    attempts = 1
    past_guesses = []

    while guess != correct_number:
        past_guesses.append(guess)
        attempts += 1
        if guess > correct_number:
            print("Too high!  Try again!")
            guess = int(input(""))
        else:
            print("Too low!  Try again!")
            guess = int(input(""))
        
    print(f"Correct!  The number was {correct_number}!")
    past_guesses.append(guess)

    if attempts > 1:
        print(f"You got it in {attempts} tries!")
        print(f"The numbers you guessed were: {past_guesses}")
    else:
        print("You got it on your first try!")
    playing_input = input("Would you like to play again? Y/N ").upper()
    if playing_input == "Y" or playing_input == "N":
        keep_playing = playing_input
    else:
        print("That is not a valid option and as such the game will end.")
        keep_playing = "N"
print("Please play again soon!")