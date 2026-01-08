import random as rand
import arcade as arc
from spaceship import my_spaceship
    
class Enemy(arc.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = rand.randint(0, game.width)
        self.center_y = game.height + 24
        self.width = 48
        self.height = 48
        self.speed = 4
        
    def move(self):
        self.center_y -= self.speed

class Game(arc.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Space Game")
        arc.set_background_color(arc.color.DARK_BLUE_GRAY)
        background = arc.Sprite(":resources:images/backgrounds/stars.png")
        background.center_x = self.width // 2
        background.center_y = self.height // 2 

        self.change_x = 0
        self.change_y = 0
        self.sprites = arc.SpriteList()
        self.enemies = []
        
        self.my_spaceship = my_spaceship(self, background.center_x)
        
        self.sprites.append(background)
        self.sprites.append(self.my_spaceship)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arc.key.LEFT or symbol == arc.key.A: 
            self.my_spaceship.change_x = -1
        elif symbol == arc.key.RIGHT or symbol == arc.key.D:
            self.my_spaceship.change_x = 1
        elif symbol == arc.key.SPACE:
            self.my_spaceship.change_x = 0
        

    def on_update(self, delta_time):
        self.my_spaceship.move()
        
        for enemy in self.enemies:
            enemy.move()
        
        if rand.randint(1, 150) == 10:    
            self.new_enemy = Enemy(self)
            self.enemies.append(self.new_enemy)
            self.sprites.append(self.new_enemy)
        
        
        
window = Game()
arc.run()
