class Player:
    def __init__(self, player):
        self.player = player
    
    @property
    def player_id(self):
        return self.player['id']

    @property
    def player_name(self):
        return self.player['name']
