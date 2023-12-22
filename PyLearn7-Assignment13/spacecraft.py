
import arcade

class Spacecraft(arcade.Sprite):
    def __init__(self):
        super.__init__()
class Enemy:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=700, title="Spacecraft Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,1280, 700, self.background)
        

window = Game()
arcade.run()



