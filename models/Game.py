from models.Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, speed, direction):
        super().__init__(x, y)
        self.speed = speed
        self.direction = direction

    def move(self):
        # Update the position of the shot based on its speed and direction
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def hit_target(self, target):
        # Check if the shot has hit the target
        return self.x == target.x and self.y == target.y