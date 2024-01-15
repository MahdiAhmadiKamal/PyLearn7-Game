import random
import time
import arcade
from spacecraft import Spacecraft
from enemy import Enemy
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=700, title="Star Wars Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft(self.width)
        # self.enemy = Enemy(self.width, self.height)
        self.enemies_list = []
        self.start_time = time.time()
        self.enemy_gap_time = 3
        self.heart_list = [None, None, None]
        

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        # self.my_hearts.draw()
        # self.enemy.draw()
        for enemy in self.enemies_list:
            enemy.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        for heart in self.heart_list: 
            heart.draw()

        # for i in range (len(self.heart_list)):
        #     self.heart_list[i].draw()

        

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

        for i in range(len(self.heart_list)):
            self.heart_list[i]=Heart()
            self.heart_list[i].center_x=30*i+30

        for enemy in self.enemies_list:
            if arcade.check_for_collision(self.me, enemy):
                print ("Game Over!")
                exit(0)
        
        # for enemy in self.enemies_list:
            
        #     if enemy.center_y + enemy.height/2 < 0:
        #         self.heart_list.pop(2)
                    
        
        # for enemy in self.enemies_list:
        #     if enemy.center_y<0: 
        #         for heart in self.heart_list:
        #             self.heart_list.pop(2)

        # j=2
        # for enemy in self.enemies_list:
        #     for i in range (len(self.heart_list)):
        #         if enemy.center_y<0: 
        #             # try:
        #                 self.heart_list.pop(j+i-2)
        #             # except(IndexError):
        #             #     pass
        #         break

        # while len(self.heart_list)>0:
        j=0
        for enemy in self.enemies_list:
            if enemy.center_y<0:
                j+=1
                if j==1:
                    # try:
                        self.heart_list.remove(self.heart_list[-1])
                    # except(IndexError):
                        # pass
                elif j==2:
                    # try:
                        self.heart_list.remove(self.heart_list[-1])
                    # except(IndexError):
                        # pass
                elif j==3:
                    # try:
                        self.heart_list.remove(self.heart_list[-1])
                    # except(IndexError):
                    #     pass



        for enemy in self.enemies_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemies_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)

        # self.enemy.move()
        self.me.move()
        
        for enemy in self.enemies_list:
            enemy.move(0.15)

        # for enemy in self.enemies_list:
        #     enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemies_list:
            if enemy.center_y + enemy.height/2 < 0:  # + enemy.height/2 <
               self.enemies_list.remove(enemy)  

        for bullet in self.me.bullet_list:
            if bullet.center_y <0:
                self.me.bullet_list.remove(bullet)

        if (self.end_time-self.start_time) >= self.enemy_gap_time:
            self.new_enemy = Enemy(self.width, self.height)
            self.enemies_list.append(self.new_enemy)
            self.start_time=time.time()

        # if random.randint(1, 80)==6:   
        #     self.new_enemy = Enemy(self.width, self.height)
        #     self.enemies_list.append(self.new_enemy)

window = Game()
arcade.run()
