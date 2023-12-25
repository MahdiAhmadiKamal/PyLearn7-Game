
import arcade


class Spacecraft(arcade.Sprite):
    def __init__(self, w):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w//2
        self.center_y= 80
        self.width = 64
        self.height = 48
        self.speed = 8
