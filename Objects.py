

class School:
    def _init_(self, id, name):
        self.id = id
        self.name = name
        self.city = "default city"
        self.state = "default state"
        self.prestige = 5
        self.budget = 10.5
    
    @property
    def Name(self):
        """For school name"""
        return self.name
    @property
    def Id(self):
        """For School ID number"""
        return self.id

class Team(School):
        
    def _init_(self, id, name, roster, coaches, recruits):
        super().__init__(id, name)
        self.roster = roster
        self.coaches = coaches
        self.recruits = recruits

