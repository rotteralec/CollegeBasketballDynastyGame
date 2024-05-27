import random

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

class Player:
    def _init(self):
        self.id = id
        self.fname = "name"
        self.lname = "name"
        self.pos = "PG"
        self.ht = 72
        self.wt = 200
        self.stats = []

    @property
    def fname(self):
        """For Player first name"""
        return self.fname
    @fname.setter
    def fname(self, value):
        self._fname = value
    
    @property
    def lname(self):
        """For Player first name"""
        return self.lname
    @lname.setter
    def lname(self, value):
        self._lname = value

    def generatePlayer(self):
        ##generate random first name
        ##First name 1387 lines
        ##Last name 2671
        print("Generate Player initiated")
        firstInd = random.randrange(1,1387)
        print(firstInd)
        lastInd = random.randrange(1,2671)
        print(lastInd)
       
        
        f = open("NBA-playerlist.csv", "r")
        names = f.readlines()
        firstName = names[firstInd]
        lastName = names[lastInd]
        firstName = firstName.split(",")
        lastName = lastName.split(",")
        print(firstName[0])
        print(lastName[1])
        f.close()
    """self.fname(firstName)
        self.lname(lastName) """
        