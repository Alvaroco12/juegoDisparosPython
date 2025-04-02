from models.Character import Character

class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def move(self):
        # Implementar lógica de movimiento del oponente
        pass

    def shoot(self):
        # Implementar lógica de disparo del oponente
        pass