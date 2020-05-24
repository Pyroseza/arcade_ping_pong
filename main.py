import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Move Paddle"
MOVEMENT_SPEED = 3

# Size of the rectangle
RECT_WIDTH = 25
RECT_HEIGHT = 25

# Ball scale
BALL_SCALE = 0.5


class Ball(arcade.Sprite):

    def __init__(self,
                 filename: str = None,
                 scale: float = 1,
                 image_x: float = 0, image_y: float = 0,
                 image_width: float = 0, image_height: float = 0,
                 center_x: float = 0, center_y: float = 0,
                 repeat_count_x: int = 1, repeat_count_y: int = 1):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height,
                         center_x, center_y, repeat_count_x, repeat_count_y)
        self.dir_x = 0
        self.dir_y = 0

    def reset_pos(self):
        # position the ball in a random location
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])

    def move(self):
        self.center_x += (MOVEMENT_SPEED * self.dir_x)
        self.center_y += (MOVEMENT_SPEED * self.dir_y)
        if self.top > SCREEN_HEIGHT:
            self.dir_y = -1
        if self.bottom < 0:
            self.dir_y = 1
        if self.right > SCREEN_WIDTH:
            self.dir_x = -1
        if self.left < 0:
            self.dir_x = 1


class Paddle:
    """CREATE THE TWO PADDLES AND MAKE THEM MOVE"""
    def __init__(self, position_x, position_y, change_x, change_y, height, width, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x  # position of x
        self.position_y = position_y  # position of y
        self.change_x = change_x  # the change in x of the paddle
        self.change_y = change_y  # the change in y of the paddle
        self.height = height  # height of the paddle
        self.width = width  # width of the paddle
        self.color = color  # color of the paddle

    def draw(self):
        """ Draw the paddle with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.height, self.width, self.color)

    def update(self):
        # Move the paddle
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the paddle hit the edge of the screen. If so, change direction
        if self.position_x < self.width:
            self.position_x = self.width

        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width

        if self.position_y < self.height:
            self.position_y = self.height

        if self.position_y > SCREEN_HEIGHT - self.height:
            self.position_y = SCREEN_HEIGHT - self.height


class Paddle_2:
    def __init__(self, position_x, position_y, change_x, change_y, height, width, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        """ Draw the paddle with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.height, self.width, self.color)

    def update(self):
        # Move the paddle
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the paddle hit the edge of the screen. If so, change direction
        if self.position_x < self.width:
            self.position_x = self.width

        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width

        if self.position_y < self.height:
            self.position_y = self.height

        if self.position_y > SCREEN_HEIGHT - self.height:
            self.position_y = SCREEN_HEIGHT - self.height


class MyGame_2(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # create the ball
        self.ball = Ball(":resources:images/pinball/pool_cue_ball.png", BALL_SCALE)
        self.ball.reset_pos()

        # Create our paddle
        self.paddle_2 = Paddle_2(25, 350, 0, 0, 25, 70, arcade.color.AUBURN)
        self.paddle = Paddle(775, 350, 0, 0, 25, 70, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.paddle_2.draw()
        self.paddle.draw()

    def on_update(self, delta_time):
        self.ball.move()
        self.paddle_2.update()
        self.paddle.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.W:
            self.paddle_2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.paddle_2.change_y = -MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.paddle.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.paddle.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.W or key == arcade.key.S:
            self.paddle_2.change_y = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.paddle.change_y = 0
















"""ADD THE BALLS TO THE GAME AND MAKE THEM BOUNCE ON PADDLE AND ON TOP/DOWN SCREEN"""




def main():
    MyGame_2(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()


if __name__ == "__main__":
    main()

