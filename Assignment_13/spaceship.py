import arcade as arc

class Spaceship(arc.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.width = 48
        self.height = 48
        self.speed = 7