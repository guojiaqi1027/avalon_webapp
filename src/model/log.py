class Log:
    def __init__(self, log):
        self.log = log

    @property
    def log_id(self):
        return self.log['id']

    @property
    def log_player(self):
        return self.log['player']

    @property
    def log_game(self):
        return self.log['game']

    @property
    def log_entities(self):
        return self.log['entities']


class RoundLog:
    def __init__(self, round_log):
        self.round_log = round_log

    @property
    def assigner(self):
        return self.round_log['assigner']

    @property
    def origin_assignment(self):
        return self.round_log['origin_assignment']

    @property
    def final_assignment(self):
        return self.round_log['final_assignment']

    @property
    def statements(self):
        return self.round_log['statements']

    @property
    def voting(self):
        return self.round_log['voting']

    @property
    def result(self):
        return self.round_log['result']
