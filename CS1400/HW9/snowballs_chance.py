import arcade

"""
Uses the arcade library to draw a house, a tree, a moon, and two snow people.

Animates one of the snowmen so it moves around the screen.
"""

# Variables for screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0,
                                      arcade.color.AIR_SUPERIORITY_BLUE)


def draw_house():
    """ Draw a house """
    # Draw the main structure of the house
    arcade.draw_rectangle_filled(650, 250, 150, 125, arcade.color.OLD_BURGUNDY)

    # Draw the roof
    arcade.draw_triangle_filled(565, 308,
                                 735, 308,
                                 650, 387, arcade.color.DARK_SLATE_GRAY)

    # Draw the door; small circle is door knob
    arcade.draw_rectangle_filled(650, 225, 37.5, 75, arcade.color.BURNT_SIENNA)
    arcade.draw_circle_filled(662, 225, 5, arcade.color.GOLDENROD)

    # Draw the windows, rectangles for panes and frames; lines for grills
    # Variable to define the size of the square windows
    window_size = 30
    # Left window
    arcade.draw_rectangle_filled(605, 250, window_size, window_size, arcade.color.BLUE_GRAY)
    # Left window frame
    arcade.draw_rectangle_outline(605, 250, window_size + 5, window_size + 5,
                                  arcade.color.WHITE, 5)
    # Left window grills
    arcade.draw_line(605, 235, 605, 265, arcade.color.WHITE, 2)
    arcade.draw_line(590, 250, 620, 250, arcade.color.WHITE, 2)
    # Right window
    arcade.draw_rectangle_filled(695, 250, window_size, window_size, arcade.color.BLUE_GRAY)
    # Right window frame
    arcade.draw_rectangle_outline(695, 250, window_size + 5, window_size + 5,
                                  arcade.color.WHITE, 5)
    # Right window grills
    arcade.draw_line(695, 235, 695, 265, arcade.color.WHITE, 2)
    arcade.draw_line(680, 250, 710, 250, arcade.color.WHITE, 2)

def draw_moon():
    """ Drawing a moon"""
    arcade.draw_circle_filled(95, 500, 75, arcade.color.BONE)

def draw_tree():
    """ Drawing a tree """
    # Draw the tree trunk
    arcade.draw_rectangle_filled(150, 217, 25, 95, arcade.color.DARK_BROWN)
    # Drawing the pine leaves
    arcade.draw_triangle_filled(110, 210, 190, 210, 150, 320, arcade.color.PINE_GREEN)

def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

    # Mouth
    arcade.draw_arc_filled(x, 195 + y, 40, 30, arcade.color.BLACK, 180, 360)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_moon()
    draw_house()
    draw_tree()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 0


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 250

def main():
    # Set up the initial canvas
    # Open an window and set a background color
    # Start drawing
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()
