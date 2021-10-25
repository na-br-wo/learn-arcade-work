"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# Import the "arcade" library.
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the dimensions (width and height)
# Set the window title to "Drawing Example"
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Finish drawing
arcade.finish_render()

# Keep the window open until someone closes it.
arcade.run()
