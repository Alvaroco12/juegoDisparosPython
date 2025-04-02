from models.Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def move(self, direction):
        # Implement movement logic here
        print(f"{self.name} moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print(f"{self.name} shoots!")