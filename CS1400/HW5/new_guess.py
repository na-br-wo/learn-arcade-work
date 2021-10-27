'''
NAME:
    New Guessing Game

DESCRIPTION:
    This program will pick a number between 1 and the user input and ask the
    user to guess the number. The user will have five guesses and the program
    will be able to handle any inputs in the wrong formats without exiting with
    an error.
'''
while True:
    try:
        max_value_input = int(input('''I'm going to pick a number. You have to guess
the same number that I pick. You have five guesses. Guess right and win a
prize. What is the highest number I can pic? '''))
        max_value = int(max_value_input)
        break
    except:
        print('Invalid response. Please try again.')
    

import random
computer_choice = random.randint(1, max_value)

count = 0

for count in range(0, 5): 
    try:
        user_guess = int(input(f'Pick a number between 1 and {max_value}: '))
        if user_guess == computer_choice:
            print('''Nice job. You win! Your prize is -- the satisfaction of
knowing you are an awesome guesser.''')
            break
        if user_guess != computer_choice:
            continue
    except ValueError:
        print('Invalid input. Please try again.')
        
        
