
import random
from Coach import *
from Recruit import *
class Team:
        
    def __init__(self, id, name, roster, recruits=[]):
        self.id = id
        self.name = name
        self.roster = roster
        self.coach = Coach("Bomb Rizzo")
        self.recruits = recruits
        self.wins = 0
        self.losses = 0





    def targetRecruit(self, _recruit):
        self.recruits.append(_recruit)
        _recruit.addSchool(self.id)

