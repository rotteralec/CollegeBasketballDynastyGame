import random
from Player import *
##Needs vague stat potentials AND recruit priorities

##Priorities: Proximity to home, School Prestige, Stadium Atmos, Facilities, College Life, Academics
#cont#Coach prestige, getting to the league, 
    ##Priorities: 
    # Proximity to home PTH
    # School Prestige SP
    #Stadium Atmos SA
    #Facilities F
    #College Life CL
    #Academics A
    #Coach prestige CP
def genPriority():
    prio = ["PTH", "SP", "SA", "F", "CL", "A", "CP", "DH"]
    random.shuffle(prio)
    return prio


##[SchoolID, interest level, visit, offer]
def genFirstFive():
    tList = []
    for i in range(0,5):
        sch = random.randrange(0,361)
        tSch = [sch]
        tSch.append(random.randrange(0,100))
        tSch.append(False)
        tSch.append(False)
        tList.append(tSch)
    return tList

    

class Recruit:




    def __init__(self, id, pos):
        self.priorities = genPriority()
        self.player = Player(id, pos)
        self.schools = genFirstFive()
        self.location = 48154
        self.hs = True



    def getPlayer(self):
        return self.player
    def getSchools(self):
        return self.schools
    def getPriority(self):
        return self.priorities