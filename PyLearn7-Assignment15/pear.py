import random
from fruit import Fruit

class Pear(Fruit):
    def __init__(self,game):
        super().__init__("pics/pear.png")
    
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.score = 2