# Bucky's Doom

"""
Displays a message to "Captain America" and asks for their input.

Calls upon the `winter_soldier.py` module, which in turn relies on `snaps`
module, so make sure they are all within the same folder.
"""

from winter_soldier import *

while True:
    """
    Loop that gathers and validates user input.

    Parameters
    ----------
    caps_response : str
        Asks the user for input.
    new_value : int
        If caps_response can be converted to an integer, does so.

    Notes
    -----
    This loop has an easter egg. If the user enters a string in response to the
    input prompt, it converts the string to the delay used in the
    bucky_words.activate() function. Otherwise, it uses the default p_value, which
    is 2 seconds.
    """
    
    caps_response = input('''Hello, Captain America. We are about to activate
                      Winter Soldier. Hopefully you won't figure out how
                      to terminate the program before we succeed. Ready? '''
                      )
    try:
        new_value = int(caps_response)
        if isinstance(new_value, int):
            activate(p_delay=new_value)
            break
    except ValueError:
        print("""We're the bad guys. We don't actually care if you are ready.
              Begin.""")
        activate()
        break
    
            
    
