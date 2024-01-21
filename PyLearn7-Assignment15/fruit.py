import arcade

class Fruit(arcade.Sprite):
    def __init__(self,pic):
        super().__init__(pic)
        
        self.width = 32
        self.height = 32
        self.change_x = 0
        self.center_y = 0