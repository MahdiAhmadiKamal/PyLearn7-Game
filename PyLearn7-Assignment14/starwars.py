import random
import arcade
# from spacecraft import Spacecraft

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
        self.speed = 4
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

        if random.randint(1, 80)==6:   
            self.new_enem = Enemy(self.width, self.height)
            self.enems.append(self.new_enem)

window = Game()
arcade.run()





