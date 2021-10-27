#Guessing Game for CS1400 by Nathan Wood

'''
NAME:
    Guessing Game

DESCRIPTION:
    The module will pick a number (the user can choose the highest possible
    number the module can pick) and the user has to try and guess what number
    the module chose. The module will display a different message depending on
    successful guessing or failure.
'''

#ask user for input (max_value) that is the highest number the module can guess
#ask for an integer as per instr. for this assignment
max_value = int(input('''I'm going to pick a number. You have to try and guess
the same number that I pick. Guess right and win a prize. What is the highest
number I can pick? '''))

import random
computer_choice = random.randint(1, max_value)

#need to convert max_value into a string to be used in the next input
max_value_for_prompt = str(max_value)

#ask user to pick a number, convert to an integer
user_choice = int(input("What number between 1 and "+max_value_for_prompt+
                        " do you choose? "
                        ))

#response with congratulations if the numbers are the same
if user_choice == computer_choice:
    print('''Nice job. You win! Your prize is -- the satisfaction of knowing
you are an awesome guesser.''')

else:
    print('Better luck next time')

print('Thank you for playing.')

