import arcade


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
