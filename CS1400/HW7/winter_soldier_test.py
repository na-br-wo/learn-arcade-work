import time
from snaps import *

bucky_words=['Longing','Rusted','Furnace','Daybreak','Seventeen','Benign',
             'Nine','Homecoming','One','Freight car']

def activate(p_delay=2):
    count = 0
    for count in range(len(bucky_words)):
        # the word "Homecoming" was displaying too large for the window that
        # opens up with this loop, the following if/else statements insures
        # "Homecoming displays correctly. Will need to be changed/removed if
        # bucky_words list is modified
        if count == 7:
            display_message(bucky_words[7],size=175) # Snaps display Homecoming
        else:
            display_message(bucky_words[count])  # Snaps Pygame Display
        time.sleep(p_delay)
        display_message('*')       # Snaps Pygame Display
        time.sleep(p_delay/2)
        count = count + 1

    display_message('Ready to comply.')
##    print('Ready to comply.')
    
if __name__ == "__main__":
    activate()
