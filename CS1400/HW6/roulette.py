##Roulette Game v1 by Nathan Wood

"""
Plays a simplified roulette game.

Parameters
----------
color : list [str]
    List of colors `Red` or `Black` for use with `get_random_color` function.

Functions
---------
get_random_color
    Choose a random color, either `Red` or `Black`.
get_num
    Choose a random integer between `0` and `36`.
play_game
    Take the player through a simple roulette game.

    This function will prompt the player for user input and validate that input
    appropriately. For example, the player must choose a color that is either
    `Red` or `Black`, and when the player chooses a number it must be an
    integer between `0` and `36`. This function will also display the message
    `I'm spinning the wheel now...` (with a delay to simulate real roulette)
    after the player enters valid inputs. It will then display a `Win` message
    or a `Lose` message.
"""

#starting off with importing `random` module for use with all following f'ns
import random
color = ['Red','Black']

def get_random_color():
    """
    Return a random number from the choices `Red` or `Black`.

    Parameters
    ----------
    color_result : random.choice(color)
        Choose a random color from the options defined on line 36.

    Returns
    -------
    str
        Random color chosen.
    """
    color_result = random.choice(color)
    return(color_result)


##Testing if the `get_random_color` function appears to be random
##count = 1
##while count < 13:
##    print("Your random color is",get_random_color())
##    count = count+1
    
    
def get_num():
    """
    Generate a random integer between 0 and 36.

    Parameters
    ----------
    num_result : random.randint(0,36)
        Choose a random integer.

    Returns
    -------
    int
        Random integer chosen.
    """
    num_result = random.randint(0, 36)
    return(num_result)
    

##Testing if the `get_num` fucntion appears to be random
##count = 1
##while count < 26:
##    print("Your random number is",get_num())
##    count = count+1

def play_game():
    """
    Take the player through a simple roulette game.

    This function will prompt the player for user input and validate that input
    appropriately. For example, the player must choose a color that is either
    `Red` or `Black`, and when the player chooses a number it must be an
    integer between `0` and `36`. This function will also display the message
    `I'm spinning the wheel now...` (with a delay to simulate real roulette)
    after the player enters valid inputs. It will then display a `Win` message
    or a `Lose` message.

    Parameters
    ----------
    color_choice_valid : bool
        Flag so color select validation loop repeats while choosing color.
    player_color : input(str)
        Player input, choosing from colors `Red` or `Black`.
    num_choice_valid : bool
        Flag so number select validation loop repeats while choosing number.
    player_num_text : str
        Text input of player number choice.
    player_num : int
        Converts player_num_text to integer.
    computer_num : int
        Calls get_num function to generate random integer.
    computer_color : str
        Calls get_random_color function to choose `Red` or `Black`.
    """

    color_choice_valid=False

    while color_choice_valid==False:
        player_color=input('''Hello, welcome to the Roulette table! Please
                     start out by picking a color: Red, or Black? 
                     ''')
        if player_color.upper() == 'QUIT':
            print('Thank you for playing Roulette.')
            return
        if player_color.upper()=='RED' or player_color.upper()=='BLACK':
            color_choice_valid=True
        else:
            print('Please choose either Red or Black.')
    print('You have selected',player_color.capitalize())

    num_choice_valid=False
    while num_choice_valid==False:
        try:
            player_num_text = input('''Please choose a number between 0 and 36.
                              ''')
            if player_num_text.upper() == 'QUIT':
                print('Thank you for playing Roulette.')
                return
            player_num = int(player_num_text)
            if player_num > -1 and player_num < 37:
                num_choice_valid=True
            else:
                print('Invalid number. Please enter a number between 0 and 36')
        except ValueError:
            print('Invalid number. Please enter a number between 0 and 36.')
    print('You have selected:',player_num)

    print('I am spinning the wheel now...')

    computer_num = get_num()
    computer_color = get_random_color()

    if (player_num == computer_num and
        player_color.upper() == computer_color.upper()):
        print('Congratulations, you win Roulette!')

    else:
        print("I'm so sorry you lost at Roulette! I bet you'll win next time")


    
