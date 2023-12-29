
import arcade


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
