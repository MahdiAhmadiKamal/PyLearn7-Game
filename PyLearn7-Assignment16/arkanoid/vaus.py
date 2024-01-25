import arcade


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

    def move(self, game):                        # for moving the Vaus using the keyboard
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
