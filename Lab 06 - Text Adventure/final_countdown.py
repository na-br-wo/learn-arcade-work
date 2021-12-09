class Room:
    """
    This is a class that represents the rooms in the adventure.
    """

    def __init__(self, description, north, south, east, west, above, below):
        """
        Method that sets up variables for Room class
        """
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.above = above
        self.below = below


def main():
    # creating the rooms
    # empty list for all rooms
    # room variable set to Class

    room_list = []

    room0_gate = Room(""" A gate breaks up a sturdy curtain wall. Outside, 
    two guards stand watch, one wearing a red surcoat, the other wearing gold.
    """, None, 1, None, None, None, None)

    room_list.append(room0_gate)

    room1_courtyard = Room(""" Inside the walls is a flat courtyard. Dead, dry
    grass crunches beneath your feet. In the center is the Lord's manor-house,
    a one-story building with paint peeling and windows shuttered. """, 0, 2,
                           None, None, None, None)

    room_list.append(room1_courtyard)

    room2_manor_house = Room(""" Motes of dust float through the few beams of 
    light that make there way through the broken shutters. The wooden floor 
    squeeks beneath your boots. The room's decor is sturdy, austere, and
    beginning to show decay. Ripped paintings and peeling wallpaper decorate
    the walls. Along the back wall, a staircase leads downwards. """, 1, None,
                             None, None, None, 3)

    room_list.append(room2_manor_house)

    room3_receiving_hall = Room(""" The stairs descend into a long receiving 
    hall paved with gray cyclopean stone. Tapestries and suits of armor line
    the walls to either side of you. To the left you see two doors, to the 
    south you see a single large oak two-paneled door, and to the right you see
    a single door along the wall. Behind the large door to the south you hear
    the muted sounds of a voice cackling with delight. """, 8, 6, 5, 7, 2, None
                                )

    room_list.append(room3_receiving_hall)

    room4_kitchen = Room(""" Pots and pans hang along the wall. Dried herbs and
    braids of garlic hang from the ceiling. The cold ashes from a cookfire pile
    up in the hearth. There is a large work table in the center for food
    preparation, and many cabinets and shelves are full of foodstuffs.""",
                         None, 5, None, None, None, None)

    room_list.append(room4_kitchen)

    room5_dining = Room(""" A large oak table dominates the room, old food
    rotting where it's been left. A cold hearth sits across from you. A door is
    to your right and your left.""", 4, 6, 3, None, None, None)

    room_list.append(room5_dining)

    room6_throne = Room(""" A lord's chair sits on a dais. A small wooden 
    clerk's table is off to the right and set slightly back. Tapestries line
    the wall. Upon the throne sits a hulking, shadowy figure""", 3, None, 5,
                        None, None, None)

    room_list.append(room6_throne)

    room7_bedroom1 = Room(""" A child's bed it pushed against the wall. A small
    wood-carved rocking horse sits in the corner. A painting of a resplendant
    Knight riding a brilliant white horse hangs on the wall opposite the foot
    of the bed. """, None, None, 3, None, None, None)

    room_list.append(room7_bedroom1)

    room8_bedroom2 = Room(""" A large curtained bed with deep maroon bedding
    sits like roytalty in the center of the far wall. A large wardrobe sits
    to the side. A bronze bathing tub is behind a paper screen. """, None,
                          None, 3, None, None, None)

    room_list.append(room8_bedroom2)

    # Lets us know where we currently are (starts at the beginning)
    current_room = 0

    # Print is testing to see if all the rooms are getting assigned correctly
    # and if list is working properly
    # print(room_list[0].description)
    #
    # print(room_list[current_room].description)

    # variable to control while loop for printing descriptions
    done = False

    while not done:
        """
        loop printing the description of each room while the done variable is
        set to False
        """
        print(room_list[current_room].description)

        # asking the player what they want to do in each room
        player_choice = input("""What direction do you want to go: (N)orth,
                              (S)outh, (E)ast, (W)est, (U)p or (D)own?                               
                              Say (Q)uit to exit the game. """)

        # all fallowing if statements take in user input and let them move
        # around the dungeon
        if player_choice.upper() == 'S' or 'SOUTH':
            next_room = room_list[current_room].south

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'N' or 'NORTH':
            next_room = room_list[current_room].north

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'E' or 'EAST':
            next_room = room_list[current_room].east

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'W' or 'WEST':
            next_room = room_list[current_room].west

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'U' or 'UP':
            next_room = room_list[current_room].above

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'D' or 'DOWN':
            next_room = room_list[current_room].below

            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif player_choice.upper() == 'Q' or 'QUIT':
            # allows user to quit the game and exit the while loop
            done = True

        else:
            print('Your input is invalid. Please try again.')




main()
