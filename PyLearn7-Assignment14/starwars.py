import random
import arcade
# from spacecraft import Spacecraft

class Spacecraft(arcade.Sprite):
    def __init__(self, w):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\my_spacecraft.png")
        self.center_x = w//2
        self.center_y= 80
        self.width = 100
        self.height = 100
        self.speed = 8

    def move(self, direction):
        if direction == "L":
            self.center_x = self.center_x - self.speed
        elif direction == "R":
            self.center_x = self.center_x + self.speed

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\enemy.png")
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = -90
        self.width = 90
        self.height = 67.5
        self.speed = 2

    def move(self):
        self.center_y -= self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=700, title="Spacecraft Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft(self.width)
        # self.enem = Enemy(self.width, self.height)
        self.enems = []

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        # self.enem.draw()
        for enem in self.enems:
            enem.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol==arcade.key.A or symbol==arcade.key.LEFT:    #left direction
            self.me.move("L")
        if symbol==arcade.key.D or symbol==arcade.key.RIGHT:   #right direction
            self.me.move("R")
        if symbol==arcade.key.SPACE:
            ...

    def on_update(self, delta_time: float):
        # self.enem.move()
        for enem in self.enems:
            enem.move()

        if random.randint(1, 80)==6:   
            self.new_enem = Enemy(self.width, self.height)
            self.enems.append(self.new_enem)

window = Game()
arcade.run()





