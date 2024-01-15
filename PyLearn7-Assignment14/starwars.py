import random
import time
import arcade


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 4
        self.change_x = 0
        self.change_y = 1

    def move(self):
        self.center_y += self.speed

class Spacecraft(arcade.Sprite):
    def __init__(self, w):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\my_spacecraft.png")
        self.center_x = w//2
        self.center_y= 80
        self.change_x = 0
        self.change_y = 0
        self.width = 100
        self.height = 100
        self.speed = 6
        self.game_width = w
        self.bullet_list = []

    # def move(self, direction):
    #     if direction == "L":
    #         self.center_x = self.center_x - self.speed
    #     elif direction == "R":
    #         self.center_x = self.center_x + self.speed

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x = self.center_x - self.speed      # or self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x = self.center_x + self.speed      # or self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment13\enemy.png")
        self.center_x = random.randint(0, w)
        self.center_y = h 
        self.angle = -90
        self.width = 90
        self.height = 67.5
        self.speed = 1

    def move(self,accel):
        self.center_y -= self.speed
        self.speed += accel

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


    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        # self.enemy.draw()
        for enemy in self.enemies_list:
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
        for enemy in self.enemies_list:
            if arcade.check_for_collision(self.me, enemy):
                print ("Game Over!")
                exit(0)

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
            if enemy.center_y + enemy.height/2 < 0:
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





