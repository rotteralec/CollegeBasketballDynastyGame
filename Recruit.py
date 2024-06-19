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

def newSchool(schoolID):
    tSch = []

    tSch.append(schoolID)#school id 0-361
    tSch.append(random.randrange(0,100)) #interest score for your team 
    tSch.append(0)#Total recruiting score
    tSch.append(0)#Total NIL Offered from School ID
    tSch.append(False)#Boolean for visit (probably change to visit object or simple arr when implemented) Needs date, bonus points calc by opponent outcome etc., 
    tSch.append(False)#Boolean for offer given
    return tSch

##[SchoolID, interest level, recruiting score, NIL, visit, offer]
def genFirstFive():
    tList = []
    for i in range(0,5):
        sch = newSchool(random.randrange(0,361))
        tList.append(sch)
    return tList

    

class Recruit:




    def __init__(self, id, pos):
        self.priorities = genPriority()
        self.player = Player(id, pos)
        self.schools = genFirstFive()
        self.location = 48154
        self.hs = True
        self.id = self.player.id



    def getPlayer(self):
        return self.player
    def getSchools(self):
        return self.schools
    
    def getMySchoolInfo(self, _schoolID): #need to implement a ?Global? my school id for seasons.
        for i in self.schools:
            if i[0] is _schoolID:
                return i

    def getPriority(self):
        return self.priorities
    def addSchool(self, _schoolID):
        self.schools.append(newSchool(_schoolID))