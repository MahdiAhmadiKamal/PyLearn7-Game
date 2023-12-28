import random
import arcade
# from spacecraft import Spacecraft

class Spacecraft(arcade.Sprite):
    def __init__(self, w):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\my_spacecraft.png")
        self.center_x = w//2
        self.center_y= 80
        self.width = 120
        self.height = 120
        self.speed = 8

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\enemy.png")
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = -90
        self.width = 100
        self.height = 75
        self.speed = 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=700, title="Spacecraft Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft(self.width)
        self.enem = Enemy(self.width, self.height)

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        self.enem.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print("yek dokme feshar dade shod.")
        
        if symbol==97:    #left direction
            self.me.center_x = self.me.center_x - self.me.speed
        if symbol==100:   #right direction
            self.me.center_x = self.me.center_x + self.me.speed

    def on_update(self, delta_time: float):
        self.enem.center_y -= self.enem.speed

window = Game()
arcade.run()





