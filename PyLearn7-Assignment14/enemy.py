import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("D:\PyLearn7\Assignments\PyLearn7-Game\PyLearn7-Assignment14\pictures\enemy.png")
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = -90
        self.width = 90
        self.height = 67.5
        self.speed = 1

    def move(self,accel):
        self.center_y -= self.speed
        self.speed += accel