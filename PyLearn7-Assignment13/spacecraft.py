
import arcade

class Spacecraft(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = 600
        self.center_y= 200
class Enemy:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=700, title="Spacecraft Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft()

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,1280, 700, self.background)
        self.me.draw()
        

window = Game()
arcade.run()





