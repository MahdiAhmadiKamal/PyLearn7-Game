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