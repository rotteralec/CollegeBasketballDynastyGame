import random


def generateFirstName():
    ##generate random first name
    ##First name 1387 lines
    ##Last name 2671
    print("Generate Player initiated")
    firstInd = random.randrange(1,1387)
    print(firstInd)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    firstName = names[firstInd]
    firstName = firstName.split(",")
    print(firstName[0])
    f.close()
    return firstName[0]
def generateLastName():
    lastInd = random.randrange(1,2671)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    lastName = names[lastInd]
    lastName = lastName.split(",")
    print(lastName[1])
    f.close()
    return lastName[1]

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
    def __init__(self):
        self.id = 0
        self.fname = generateFirstName()
        self.lname = generateLastName()
        self.pos = "PG"
        self.ht = 72
        self.wt = 200
        self.stats = []



        