import random as rand
import arcade as arc
from spaceship import Spaceship
    
class Enemy(arc.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = rand.randint(0, game.width)
        self.center_y = game.height + 24
        self.width = 48
        self.height = 48
        self.speed = 4

class Game(arc.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Space Game")
        arc.set_background_color(arc.color.DARK_BLUE_GRAY)

        self.sprites = arc.SpriteList()
        background = arc.Sprite(":resources:images/backgrounds/stars.png")
        background.center_x = self.width // 2
        background.center_y = self.height // 2 
        
        self.spaceship = Spaceship(self)
        self.enemy = Enemy(self)
        
        self.sprites.append(background)
        self.sprites.append(self.spaceship)
        self.sprites.append(self.enemy)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97: 
            self.spaceship.center_x -= self.spaceship.speed
        elif symbol == 100:
            self.spaceship.center_x += self.spaceship.speed

    def on_update(self, delta_time):
        self.enemy.center_y -= self.enemy.speed
window = Game()
arc.run()
