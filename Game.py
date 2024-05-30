import random




class Game:

    def __init__(self, home, away, date, NF):
        self.id = 0
        self.home = home
        self.away = away
        self.date = date
        self.NF = NF
        self.homescore = 0
        self.awayscore = 0
        