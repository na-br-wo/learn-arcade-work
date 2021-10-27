## Winter Soldier

"""
Displays words from a list with a delay between each word.

Parameters
----------
bucky_words : list
    List of words from Captain America: Winter Soldier.

Notes
-----
Imports `time` module and `snaps` module. !!Make sure snaps is in the same
folder as this file or this will not work!! Also, must install pygame on your
PATH; snaps module calls pygame.
"""

import time
from snaps import *

bucky_words=['Longing','Rusted','Furnace','Daybreak','Seventeen','Benign',
             'Nine','Homecoming','One','Freight car']

def activate(p_delay=2):
    """
    Activates the screen which displays the list bucky_words in red font.

    Parameters
    ----------
    count : int
        Used to run the for loop.
    p_delay : int
        The amount of time, in seconds, each word will flash on the screen.

    Notes
    -----
    display_message() is a function called from `snaps` module. The `count` is
    used to tweak certain words specific to this bucky_list, can be deleted and
    tweaked if you are using a different list of words.
    """
    count = 0
    for count in range(len(bucky_words)):
        # the word "Homecoming" was displaying too large for the window that
        # opens up with this loop, the following if/else statements insures
        # "Homecoming" displays correctly. Will need to be changed/removed if
        # bucky_words list is modified
        if count == 7:
            display_message(bucky_words[7],size=175) # Snaps display Homecoming
        else:
            display_message(bucky_words[count])  # Snaps Pygame Display
        time.sleep(p_delay)
        display_message('*',size=350)       # Snaps Pygame Display
        time.sleep(p_delay/2)
        count = count + 1

    display_message('Ready to comply.')
##    print('Ready to comply.')  ## Regular print statement used for testing
                                 ## if not using snaps/pygame
    
if __name__ == "__main__":
    activate()
