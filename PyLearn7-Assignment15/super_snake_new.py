import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self,pic):
        super().__init__(pic)
        self.width = 32
        self.height = 32
        # self.center_x = random.randint(10, game.width-10)
        # self.center_y = random.randint(10, game.height-10)
        self.change_x = 0
        self.center_y = 0

class Apple(Fruit):
    def __init__(self,game):
        super().__init__("pics/apple.png")
        
        # self.width = 32
        # self.height = 32
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.score = 1
        # self.change_x = 0
        # self.change_y = 0

class Pear(Fruit):
    def __init__(self,game):
        super().__init__("pics/pear.png")
    
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.score = 2

class Chili(Fruit):
    def __init__(self,game):
        super().__init__("pics/chili.png")
    
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.score = -1

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.GREEN
        self.color2 = arcade.color.ORANGE
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        if self.score == 0:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        else:
            for part in self.body:
                if self.body.index(part)%2==0:
                    arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color)
                elif self.body.index(part)%2!=0:
                    arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color2)
            
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x': self.center_x, 'y': self.center_y})
        
        if len(self.body)> self.score:
            self.body.pop(0) 

    def eat(self, food):
        self.score += food.score
        if self.score == 0:
            game.condition = "Game Over"

        del food
        print("score:", self.score)
       

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V.1.0 🐍")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.foods = [Apple(self), Pear(self), Chili(self)]
        self.condition = ""
            
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        for food in self.foods:

            food.draw()
        
        arcade.draw_text(f"score: {self.snake.score}", self.width-100, 15, arcade.color.BLACK, 15)

        if self.condition == "Game Over":
            arcade.start_render()
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over",self.width/5, self.height/2, arcade.color.BLACK, 45)
            
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if self.snake.center_x>self.width or self.snake.center_x<0:
            self.condition = "Game Over"
            
        if self.snake.center_y>self.height or self.snake.center_y<0:
            self.condition = "Game Over"

        for food in self.foods:
            if arcade.check_for_collision(self.snake, food):
                self.snake.eat(food)
                print(food.score)
                self.foods = [Apple(self), Pear(self), Chili(self)]

        # for part in self.snake.body:
        #     if self.snake.body[0]['x']==part['x']:
        
                



    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()


