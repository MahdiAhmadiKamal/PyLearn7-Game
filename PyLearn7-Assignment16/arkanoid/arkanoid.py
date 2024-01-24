import arcade

class Ball(arcade.Sprite):
    def __init__(self, player):
        super().__init__("pics\klipartz.com.png")
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height
        self.width = 25
        self.height = 25
        self.change_x = 0
        self.change_y = 0
        self.speed = 5

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Block(arcade.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.width = 60
        self.height = 30

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Vaus(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = 40
        self.speed = 4
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.GREEN
        self.width = 80
        self.height = 22
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        # arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width+3, self.height, arcade.color.DARK_PINK, border_width=3)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title="Super Arkanoid 🕹")
        # arcade.set_background_color(arcade.color.PERSIAN_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.player = Vaus(self)
        self.ball = Ball(self.player)
        self.block = Block(40, self.height//2, arcade.color.RED_BROWN)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.player.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.ball.center_y > self.player.center_y + self.player.height and \
            self.player.width//2 < x < self.width - self.player.width//2:
            self.player.center_x = x
        elif self.player.width//2 < x < self.width - self.player.width//2:
            self.player.center_x = x
            self.ball.center_x = x


    def on_update(self, delta_time: float):
        self.ball.move()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.change_x = 0.25
            self.ball.change_y = 1
            
            
            



game = Game()
arcade.run()