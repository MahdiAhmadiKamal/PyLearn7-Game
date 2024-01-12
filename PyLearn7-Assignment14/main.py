import random
import arcade
from spacecraft import Spacecraft
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=700, title="Star Wars Game")
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

        for bullet in self.me.bullet_list:
            bullet.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol==arcade.key.A or symbol==arcade.key.LEFT:    #left direction
            # self.me.move("L")
            self.me.change_x = -1
        elif symbol==arcade.key.D or symbol==arcade.key.RIGHT:   #right direction
            # self.me.move("R")
            self.me.change_x = 1
        elif symbol==arcade.key.S or symbol==arcade.key.DOWN:   #stop
            self.me.change_x = 0
        elif symbol==arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0   
        
    def on_update(self, delta_time: float):
        for enem in self.enems:
            if arcade.check_for_collision(self.me, enem):
                print ("Game Over!")
                exit(0)

        for enem in self.enems:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enem, bullet):
                    self.enems.remove(enem)
                    self.me.bullet_list.remove(bullet)

        # self.enem.move()
        self.me.move()

        for enem in self.enems:
            enem.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enem in self.enems:
            if enem.center_y < 0:
               self.enems.remove(enem)  
               
        if random.randint(1, 80)==6:   
            self.new_enem = Enemy(self.width, self.height)
            self.enems.append(self.new_enem)

window = Game()
arcade.run()
