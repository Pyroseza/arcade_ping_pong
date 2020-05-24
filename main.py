import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Ping Pong"
MOVEMENT_SPEED = 3

# Sprite draw scale
DRAW_SCALE = 0.5


class Ball(arcade.Sprite):
    dir_x = 0
    dir_y = 0

    def reset_pos(self):
        # position the ball in a random location
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])

    def check_collisions(self, paddle_list):
        # TODO: round should end or the game should end if the below collision occurred
        # has the ball gone off to the side of the screen
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.dir_x = 0
            self.dir_y = 0

        # has the ball gone above the screen height
        if self.top > SCREEN_HEIGHT:
            self.dir_y = -1
        # has the ball gone below the screen height
        if self.bottom < 0:
            self.dir_y = 1

        # test if it has collided with a paddle
        hits = self.collides_with_list(paddle_list)
        if hits:
            self.dir_x = 1 if self.dir_x == -1 else -1

    def update(self, paddle_list):
        # always move the ball first
        self.center_x += (MOVEMENT_SPEED * self.dir_x)
        self.center_y += (MOVEMENT_SPEED * self.dir_y)
        self.check_collisions(paddle_list)


class Paddle(arcade.Sprite):
    dir_y = 0

    def reset_pos(self, x, y):
        self.center_x = x
        self.center_y = y

    def check_bounds(self):
        # has the paddle gone above the screen height
        if self.top > SCREEN_HEIGHT and self.change_y == 1:
            self.change_y = 0
        # has the ball gone below the screen height
        if self.bottom < 0 and self.change_y == -1:
            self.change_y = 0

    def update(self):
        # first check the bounds make sure we don't go where we can't
        self.check_bounds()
        # Move the paddle
        self.center_y += (MOVEMENT_SPEED * self.change_y)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # create the ball
        self.ball = Ball(":resources:images/pinball/pool_cue_ball.png", DRAW_SCALE)
        self.ball.reset_pos()

        # Create our paddle objects
        self.paddles = arcade.SpriteList()
        self.paddle_1 = Paddle(":resources:images/tiles/boxCrate.png", DRAW_SCALE)
        self.paddle_1.reset_pos(self.paddle_1.width, SCREEN_HEIGHT/2)
        self.paddles.append(self.paddle_1)
        self.paddle_2 = Paddle(":resources:images/tiles/boxCrate.png", DRAW_SCALE)
        self.paddle_2.reset_pos(SCREEN_WIDTH - self.paddle_2.width, SCREEN_HEIGHT/2)
        self.paddles.append(self.paddle_2)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.paddle_1.draw()
        self.paddle_2.draw()

    def on_update(self, delta_time):
        self.paddle_1.update()
        self.paddle_2.update()
        self.ball.update(self.paddles)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.W:
            self.paddle_1.change_y = 1
        elif key == arcade.key.S:
            self.paddle_1.change_y = -1
        if key == arcade.key.UP:
            self.paddle_2.change_y = 1
        elif key == arcade.key.DOWN:
            self.paddle_2.change_y = -1

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.W or key == arcade.key.S:
            self.paddle_1.change_y = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.paddle_2.change_y = 0


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()


if __name__ == "__main__":
    main()

