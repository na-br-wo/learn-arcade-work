#Random_Walk

'''
NAME:
    Random Walk

DESCRIPTION:
    This module will ask the user for a low and a high input, accounting for
    the wrong inputs without exiting on an error. It will then take the user on
    a "random number walk" between their two inputs until certain condtions are
    met, at which point it will end.
'''

#the while loop for the lower value
while True:
    try:
        #ask the user to chose the low value
        low_user_input = input('''Hello, this exercise will be a "directed" Random
Walk. First, please select an integer for your lowest value. It cannot be lower
than 0. ''')
        low_val = int(low_user_input)
        if low_val < 0:
            raise ValueError
        break
    except ValueError:
        print('Please give an integer response (>=0).')

#the while loop for the higher value
while True:
    try:
        #ask the user to choose the high value
        high_user_input = input('''Now, select an integer for your highest
value. It must be >=20 and <=1000. ''')
        high_val = int(high_user_input)
        if high_val < 20:
            raise ValueError
        if high_val > 1000:
            raise ValueError
        break
    except ValueError:
        print('Please give an integer response (>=20 and =<1000).')

cur_position = ((low_val+high_val/2))

import random #importing random for use in next loop
walk_flag = True #setting up the boolean variable for the next loop

while walk_flag == True:
    #asking user if they want to go up or down
    walk_input = input(f'''{cur_position} is your current position. Would you
like to go up or down? ''')
    if walk_input.upper() == 'UP':
        cur_position = random.randint(low_val, high_val) + cur_position
        if cur_position > high_val:
            walk_flag = False
    elif walk_input.upper() == 'DOWN':
        cur_position = cur_position - random.randint(low_val, high_val)
        if cur_position < low_val:
            walk_flag = False
    elif walk_input.upper() == 'QUIT':
        walk_flag = False
    else:
        print('Please choose up, down, or quit.')
        walk_flag = True
        
