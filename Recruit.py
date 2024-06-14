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

class Recruit:




    def __init__(self, id, pos):
        self.priorities = genPriority()
        self.player = Player(id, pos)
        self.schools = []
