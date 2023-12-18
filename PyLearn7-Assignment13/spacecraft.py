
import arcade

class Spacecraft:
    ...

class Enemy:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("session 13\camera.jpg")

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(10,20,500, 500, self.background)
        


window = Game()
arcade.run()