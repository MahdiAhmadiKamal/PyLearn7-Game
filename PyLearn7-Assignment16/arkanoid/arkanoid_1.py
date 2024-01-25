import arcade

class Ball(arcade.Sprite):
    def __init__(self, player):
        super().__init__("pics\klipartz.com.png")
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height
        self.radius = 12.5
        self.width = 2 * self.radius
        self.height = 2 * self.radius
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
        # self.row = []


    def draw(self):
        # for i in range (7):
        #     arcade.draw_rectangle_filled(self.center_x+63*i, self.center_y, self.width, self.height, self.color)
        
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
        self.block_row = []
        for j in range (4):
            for i in range (8):
                if j%2==0:
                    self.block = Block(35+61*i, self.height//2 + 35*j, arcade.color.RED_BROWN)
                    self.block_row.append(self.block)
                elif j%2==1:
                    self.block = Block(35+61*i, self.height//2 + 35*j, arcade.color.RED_ORANGE)
                    self.block_row.append(self.block)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.player.draw()
        self.ball.draw()
        for self.block in self.block_row:
            self.block.draw()
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
        if arcade.check_for_collision(self.ball, self.player):
            self.ball.change_y *= -1
        
        if self.ball.center_x < self.ball.radius or self.ball.center_x > self.width - self.ball.radius:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height - self.ball.radius:
            self.ball.change_y *= -1


        for i in range (len(self.block_row)):
            try:
                if arcade.check_for_collision(self.ball, self.block_row[i]):
                    self.ball.change_y *= -1
                    del self.block_row[i]
            except(IndexError):
                pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.change_x = 0.15
            self.ball.change_y = 1
            
            

game = Game()
arcade.run()