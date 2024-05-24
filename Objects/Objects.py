class School:
    def _init_(self, id, name):
        self.id = id
        self.name = name
        self.city = "default city"
        self.state = "default state"
        self.prestige = 5
        self.budget = 10.5

class Team(School):
    def _init_(self, id, name, roster, coaches, recruits):
        super().__init__(id, name)
        self.roster = roster
        self.coaches = coaches
        self.recruits = recruits

class Player:
    def _init(self, id, name, pos, ht, wt, stats):
        self.id = id
        self.name = name
        self.pos = pos
        self.ht = ht
        self.wt = wt
        self.stats = stats
        