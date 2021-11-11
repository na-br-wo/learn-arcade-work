"""
This simple animation example shows how to use classes to animate
multiple objects on the screen at the same time.

Because this is redraws the shapes from scratch each frame, this is SLOW
and inefficient.

Using buffered drawing commands (Vertex Buffer Objects) is a bit more complex,
but faster.

See
https://api.arcade.academy/en/latest/examples/index.html#faster-drawing-with-shapeelementlists
for this same example using shape element lists.

Also, any Sprite class put in a SpriteList and drawn with the SpriteList will
be drawn using Vertex Buffer Objects for better performance.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.shapes_buffered
"""

import arcade
import random
import timeit

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shapes and Fish! Non-buffered"

RECT_WIDTH = 50
RECT_HEIGHT = 50

NUMBER_OF_SHAPES = 123


class Shape:
    """ Generic base shape class """
    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_angle = delta_angle
        self.color = color

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.angle += self.delta_angle
        if self.x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if self.y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if self.x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if self.y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1


class Ellipse(Shape):
    """ Ellipse based off generic Shape class """

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color, self.angle)


class Rectangle(Shape):
    """ Rectangle based off generic Shape class """

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)


class Line(Shape):
    """
    Line based of generic Shape class
    It is angled
    """

    def draw(self):
        arcade.draw_line(self.x, self.y,
                         self.x + self.width, self.y + self.height,
                         self.color, 2)


class Fish(Shape):
    """
    Fish drawn, based off generic Shape class

    Has an ellipse for the body, triangle for tail, circle for eye
    Flips direction based on self.delta_x

    Fish do not move on the y-axis so the move() function only deals
    with the x-axis
    """
## Change the fish variable, adding super and other things if necessary
    def draw(self):
        if self.delta_x >= 0:
            arcade.draw_ellipse_filled(self.x, self.y, self.width, self.width/2,
                                       self.color, 0)

            arcade.draw_triangle_filled(self.x - self.width/2, self.y, # x1 and y1
                                        self.x - self.width/1.7,       # x2
                                        self.y + (self.width/4),       # y2
                                        self.x - self.width/1.7,       # x3
                                        self.y - (self.width/4),       # y3
                                        self.color)

            arcade.draw_circle_filled(self.x + self.width/3,
                                      self.y + self.width/12,
                                      self.width/15,
                                      color = arcade.color.BLACK)
        else:
            arcade.draw_ellipse_filled(self.x, self.y, self.width, self.width / 2,
                                       self.color, 0)

            arcade.draw_triangle_filled(self.x + self.width / 2, self.y,  # x1 and y1
                                        self.x + self.width / 1.7,  # x2
                                        self.y - (self.width / 4),  # y2
                                        self.x + self.width / 1.7,  # x3
                                        self.y + (self.width / 4),  # y3
                                        self.color)

            arcade.draw_circle_filled(self.x - self.width / 3,
                                      self.y + self.width / 12,
                                      self.width / 15,
                                      color=arcade.color.BLACK)

    def move(self):
        """ Controls movement for fish, "bounces" off edge of screen """
        self.x += self.delta_x
        if self.x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if self.x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None

        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.shape_list = []

        for i in range(NUMBER_OF_SHAPES):
            """ Draws the shapes, randomizing variables """
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            width = random.randrange(10, 30)
            height = random.randrange(10, 30)
            angle = random.randrange(0, 360)

            d_x = random.randrange(-3, 4)
            d_y = random.randrange(-3, 4)
            d_angle = random.randrange(-3, 4)

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            alpha = random.randrange(256)

            shape_type = random.randrange(3)
            # shape_type = 2

            if shape_type == 0:
                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                  d_angle, (red, green, blue, alpha))
            elif shape_type == 1:
                shape = Ellipse(x, y, width, height, angle, d_x, d_y,
                                d_angle, (red, green, blue, alpha))
            elif shape_type == 2:
                shape = Line(x, y, width, height, angle, d_x, d_y,
                             d_angle, (red, green, blue, alpha))

            self.shape_list.append(shape)

        fish_count = 5
        for i in range(fish_count):
            """
            Draws the fish, can change fish_count to change amount of fish
            """
            x = random.randrange(15, SCREEN_WIDTH - 15)
            y = random.randrange(15, SCREEN_HEIGHT - 15)
            width = random.randrange(10, 30)
            height = random.randrange(10, 30)
            d_x = random.randrange(-3, 4)

            fish = Fish(x, y, width * 4, height, angle, d_x, d_y,
                         d_angle, color=arcade.color.ORANGE)

            self.shape_list.append(fish)


    def on_update(self, dt):
        """ Move everything """
        start_time = timeit.default_timer()

        for shape in self.shape_list:
            """ Calls move function for all shapes in the list """
            shape.move()

        self.processing_time = timeit.default_timer() - start_time

    def on_draw(self):
        """
        Render the screen.
        """
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        if self.frame_count % 60 == 0:
            """ Starting the FPS counter """
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

        arcade.start_render()

        arcade.set_background_color(arcade.color.PICTON_BLUE)

        for shape in self.shape_list:
            """ Drawing the shapes form the shape list """
            shape.draw()

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 20, arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 16)

        if self.fps is not None:
            """ Displays FPS counter on screen """
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()