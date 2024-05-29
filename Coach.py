import random

def GenerateStats():
    ##Offensive, Defensive, Training, Recruiting
    stats = []
    off = random.randrange(20,100)
    def = random.randrange(20,100)
    tra = random.randrange(20,100)
    rec = random.randrange(20,100)




class Coach():
    



    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.stats = GenerateStats()