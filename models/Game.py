class Game:
    def __init__(self, player, opponent):
        self.score = 0
        self.player = player
        self.opponent = opponent
        self.is_running = False

    def start(self):
        self.is_running = True
        print("Game started!")

    def update(self):
        if self.is_running:
            # Update game logic here
            print("Game is updating...")

    def end_game(self):
        self.is_running = False
        print("Game over!")