
import random
from Coach import *
class Team:
        
    def __init__(self, name, roster, recruits):
        self.id = 0
        self.name = name
        self.roster = roster
        self.coach = Coach("Bomb Rizzo")
        self.recruits = recruits
