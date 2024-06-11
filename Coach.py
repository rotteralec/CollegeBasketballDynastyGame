import random

def GenerateStats():
    ##Offensive, Defensive, Training, Recruiting
    statsDict = {}
    statsDict["Off"] = random.randrange(20,100)
    statsDict["Def"] = random.randrange(20,100)
    statsDict["Tra"] = random.randrange(20,100)
    statsDict["Rec"] = random.randrange(20,100)
    return statsDict




class Coach():


    def __init__(self, name):
        self.id = 0
        self.name = name
        self.role = "H"
        self.stats = GenerateStats()
        self.level = 0
        self.recAcc = 3