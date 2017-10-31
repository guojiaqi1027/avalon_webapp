class Game:
    def __init__(self, game):
        self.game = game
    
    @property
    def game_id(self):
        return self.game['id']

    @property
    def game_players(self):
        return self.game['players']

    @property
    def game_roles(self):
        return self.game['roles']

    @property
    def game_assignment(self):
        return self.game['assignment']

    @property
    def game_result(self):
        return self.game['result']
