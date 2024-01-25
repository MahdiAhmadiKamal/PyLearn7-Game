import arcade

class Ball(arcade.Sprite):
    def __init__(self, player):
        super().__init__("pics&sounds/ball.png")
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height
        self.radius = 12.5
        self.width = 2 * self.radius
        self.height = 2 * self.radius
        self.change_x = 0
        self.change_y = 0
        self.speed = 6

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
        
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Vaus(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = 40
        self.speed = 6
        self.change_x = 0
        self.change_y = 0
        self.color = arcade.color.GREEN
        self.width = 90
        self.height = 22
        self.score = 0

    def move(self):                        # for moving the Vaus using the keyboard
        if game.ball.center_y > self.center_y + self.height//2 + game.ball.radius: 
            # when the ball is not on the Vaus
            if self.change_x == -1:
                if self.center_x - self.width//2 > 0:
                    self.center_x = self.center_x - self.speed
            elif self.change_x == 1:
                if self.center_x + self.width//2 < game.width:
                    self.center_x = self.center_x + self.speed 

        else:                             
            # when the ball is on the Vaus
            if self.change_x == -1:
                if self.center_x - self.width//2 > 0:
                    self.center_x = self.center_x - self.speed
                    game.ball.center_x = game.ball.center_x - self.speed
            elif self.change_x == 1:
                if self.center_x + self.width//2 < game.width:
                    self.center_x = self.center_x + self.speed
                    game.ball.center_x = game.ball.center_x + self.speed 

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
        self.condition = ""
        self.count = 0
        self.sound_1 = arcade.sound.load_sound("pics&sounds/ball_sound.wav")

        for j in range (4):
            for i in range (6):
                if j%2==0:
                    self.block = Block(95+61*i, self.height//2 + 35*j, arcade.color.RED_BROWN)
                    self.block_row.append(self.block)
                elif j%2==1:
                    self.block = Block(95+61*i, self.height//2 + 35*j, arcade.color.RED_ORANGE)
                    self.block_row.append(self.block)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        arcade.draw_text(f"score: {self.player.score}", 20, self.height-50, arcade.color.WHITE,
                          25, font_name=("broadway"))
        self.player.draw()
        self.ball.draw()
        for self.block in self.block_row:
            self.block.draw()

        if self.condition == "Game Over":
            arcade.start_render()
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over",self.width/8, self.height/2, arcade.color.RED_PURPLE,
                              45, font_name=("broadway"))

        if self.condition == "Win":
            arcade.start_render()
            arcade.draw_text("You Win!",self.width/5, self.height/2, arcade.color.RED_PURPLE,
                              45, font_name=("broadway"))
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.ball.center_y > self.player.center_y + self.player.height//2 + self.ball.radius and \
            self.player.width//2 < x < self.width - self.player.width//2:
            self.player.center_x = x
        elif self.player.width//2 < x < self.width - self.player.width//2:
            self.player.center_x = x
            self.ball.center_x = x

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE and \
        self.ball.center_y >= self.player.center_y + self.player.height//2:
            self.ball.change_x = 0.25
            self.ball.change_y = 1

        if symbol==arcade.key.A:        #left direction
            self.player.change_x = -1
        elif symbol==arcade.key.D:      #right direction
            self.player.change_x = 1
        
            
    def on_key_release(self, symbol: int, modifiers: int):
        self.player.change_x = 0  

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player.move()                  # for moving the Vaus using the keyboard
        if arcade.check_for_collision(self.ball, self.player):
            self.ball.change_y *= -1
        
        if self.ball.center_x < self.ball.radius or self.ball.center_x > self.width - self.ball.radius:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height - self.ball.radius:
            self.ball.change_y *= -1

        if self.count == 3:
            self.condition = "Game Over"
        elif self.ball.center_y + 10*self.ball.radius < 0:
            self.player.score -= 1
            del self.ball
            self.ball = Ball(self.player)
            self.count += 1
    

        for i in range (len(self.block_row)):
            try:
                if arcade.check_for_collision(self.ball, self.block_row[i]):
                    self.ball.change_y *= -1
                    arcade.sound.play_sound(self.sound_1)
                    del self.block_row[i]
                    self.player.score += 1
                    if len((self.block_row))==0:
                        self.condition = "Win"
            except(IndexError):
                pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and \
        self.ball.center_y >= self.player.center_y + self.player.height//2:
            self.ball.change_x = 0.25
            self.ball.change_y = 1

        
            
            

game = Game()
arcade.run()