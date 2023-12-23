
import arcade

class Spacecraft(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width//2
        self.center_y= 200
        self.width = 64
        self.height = 48
class Enemy:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=700, title="Spacecraft Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spacecraft(self)

    # methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height, self.background)
        self.me.draw()
        

window = Game()
arcade.run()





