#Casino Games
#Casino Games v1 by Nathan Wood

"""
Offers choice of two casino games for the user to play.

Games are `Roulette` or `Coin Toss`.

Parameters
----------
game_choice_valid : bool
    Flag to let the while loop run.
casino_choice : input(str)
    Player input, can choose which game to play, or quit.

Notes
-----
Imports `coin_toss.py` and `roulette.py` modules, so make sure they are in the
same folder as this file.
"""


import coin_toss
import roulette

game_choice_valid=False
while game_choice_valid==False:
    casino_choice = input(
          '''
          Welcome to the Casino. Would you like to play?
          Type [1] to play Roulette
          Type [2] to flip a coin
          Type "quit" if you want to leave.

          What's your choice?
          ''')
    if casino_choice.upper() == 'QUIT':
        print('Thank you for visiting the Casino.')
        game_choice_valid=True
    elif casino_choice == '1':
        roulette.play_game()
    elif casino_choice == '2':
        coin_toss.play_game()
    else:
        print('''Please choose [1], [2], or "quit"''')

