
import random
from Coach import *
from Recruit import *
from Player import *





class Team:
        
    def __init__(self, id, name, roster, recruits=[]):
        self.id = id
        self.name = name
        self.roster = roster
        self.coach = Coach("Bomb Rizzo")
        self.recruits = recruits
        self.wins = 0
        self.losses = 0
        self.offense = 0
        self.defence = 0
        self.overall = 0


    def calcRatings(self):
        tOff = 0
        tDef = 0
        tOvr = 0
        count = 0
        for i in self.roster:
            tRate = i.getRatings()
            tOff += tRate[1]
            tDef += tRate[2]
            tOvr += tRate[0]
            count += 1
        self.offense = round(tOff/count)
        self.defence = round(tDef/count)
        self.overall = round(tOvr/count)

    def getRatings(self):
        return [self.overall, self.offense, self.defence]
    def targetRecruit(self, _recruit):
        self.recruits.append(_recruit)
        _recruit.addSchool(self.id)

    def getTargetedRecruit(self, _recruitID):
        for i in self.recruits:
            if i.id is _recruitID:
                return i
    def getRoster(self):
        return self.roster

    

