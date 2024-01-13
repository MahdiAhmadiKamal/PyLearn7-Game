import random
import time
import arcade
from spacecraft import Spacecraft
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=700, title="Star Wars Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft(self.width)
        # self.enemy = Enemy(self.width, self.height)
        self.enemies = []
        self.start_time = time.time()
        self.enemy_gap_time = 3

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        # self.enemy.draw()
        for enemy in self.enemies:
            enemy.draw()

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
        self.end_time = time.time()
        for enemy in self.enemies:
            if arcade.check_for_collision(self.me, enemy):
                print ("Game Over!")
                exit(0)

        for enemy in self.enemies:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemies.remove(enemy)
                    self.me.bullet_list.remove(bullet)

        # self.enemy.move()
        self.me.move()
        
        for enemy in self.enemies:
            enemy.move(0.2)

        # for enemy in self.enemies:
        #     enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemies:
            if enemy.center_y < 0:
               self.enemies.remove(enemy)  

        if (self.end_time-self.start_time) >= self.enemy_gap_time:
            self.new_enemy = Enemy(self.width, self.height)
            self.enemies.append(self.new_enemy)
            self.start_time=time.time()

        # if random.randint(1, 80)==6:   
        #     self.new_enemy = Enemy(self.width, self.height)
        #     self.enemies.append(self.new_enemy)

window = Game()
arcade.run()
