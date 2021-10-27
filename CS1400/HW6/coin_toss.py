#Coin Toss Game v1 by Nathan Wood

"""
Plays a coin toss game.

Parameters
----------
coin : list [str]
    List giving two coin options, `Heads` or `Tails`.

Functions
---------
flip
    Generates a randomized coin flip.
play_game
    Take the player through the coin flip game.

    Prompt the player to choose `Heads` or `Tails`, compares this against the
    computer's randomized coin flip, and tells the user if they win or not.
    Allows the user to quit.
"""

import random
coin = ['Heads','Tails']

def flip():
    """
    Generates a random coin flip.

    Returns
    -------
    str
        `Heads` or `Tails`.
    """
    result = random.choice(coin)
    return(result)

def play_game():
    """
    Take the player through the coin flip game.

    Compares the user choice of `Heads` or `Tails` with computer generated coin
    flip. Informs the user if they win or lose. Allows user to quit.

    Parameters
    ----------
    coin_choice_valid : bool
        Flag so that the coin choice validation loop repeats.
    player_choice : input(str)
        Ask the user to choose `Heads` or `Tails`.
    computer_choice : str
        Calls flip function to generate a coin flip.
    """
    coin_choice_valid=False
    while coin_choice_valid==False:
        player_choice = input('''Hello, I'm going to flip a coin. You can choose
                        Heads or Tails. ''')
        if player_choice.upper() == 'QUIT':
            print('Thank you for playing Coin Toss.')
            return
        if player_choice.upper()=='HEADS' or player_choice.upper()=='TAILS':
            coin_choice_valid=True
        else:
            print('Please choose either Heads or Tails.')
    print('You have selected',player_choice.capitalize())

    print('I am going to flip the coin...')

    computer_choice = flip()

    if player_choice.upper() == computer_choice.upper():
        print("It's",player_choice.capitalize())
        print('Congratulations, you win Coin Toss!')
    else:
        print("It's",computer_choice.capitalize())
        print("I'm so sorry you lost at Coin Toss. I bet you'll win next time."
              )


#The code below helps test the randomness of the flips() function, but only
        #when you are running the main file, not when importing coin_toss
        #into another module
def flips(p_iterations, p_toss_string = 'Toss a coin'):
    """
    Call flip p_iterations times to run a string of coin tosses.

    This is a test to verify the random coin flip is working properly, ie
    generating random `Heads` or `Tails` results.

    Parameters
    ----------
    p_iterations : int
        The amount of times the coin test flip will flip.

    Notes
    -----
    Due to the `if` statement at the bottom of the code, this function will
    only run if this specific file is being run. You can import this module
    and run the normal `flip` function without generating the test flips.
    """        
    for i in range(p_iterations):
        print(p_toss_string,':',flip())


if __name__ == '__main__':
    flips(13, 'Test flip')        
