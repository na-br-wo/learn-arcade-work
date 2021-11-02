# import arcade
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
#
# arcade.set_background_color(arcade.color.WHITE)
#
# ##arcade.start_render()
#
# # Instead of this:
# # arcade.draw_circle_filled(400, 300, 50, arcade.color.FOREST_GREEN)
# # do this:
# arcade.draw_circle_filled(SCREEN_WIDTH / 2,
#                           SCREEN_HEIGHT / 2,
#                           50,
#                           arcade.color.FOREST_GREEN)
#
# arcade.finish_render()
# ##arcade.run()
r = 8.5
v = 2 * (3.14 * r)

print(f"The area of the circle is {round(v, 2)} square inches.")
