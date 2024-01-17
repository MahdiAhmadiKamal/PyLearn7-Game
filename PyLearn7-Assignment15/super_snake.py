import random
import arcade


class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("apple2.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(20, game.width-20)
        self.center_y = random.randint(20, game.height-20)
        self.change_x = 0
        self.center_y = 0

class Snake:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V.1.0 🐍")
        arcade.set_background_color(arcade.color.KHAKI)

        self.food = Apple(self)

    def on_draw(self):
        arcade.start_render()
        self.food.draw()

        arcade.finish_render()

if __name__ == "__main__":
    game = Game()
    arcade.run()


