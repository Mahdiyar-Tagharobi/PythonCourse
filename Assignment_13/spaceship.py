import arcade as arc

class my_spaceship(arc.Sprite):
    def __init__(self, game, w):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.game_width = game.width
        self.width = 48
        self.height = 48
        self.speed = 7
        
    def move(self):
        if self.change_x == -1:
            if self.center_x < 0:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x > self.game_width:
                self.center_x += self.speed