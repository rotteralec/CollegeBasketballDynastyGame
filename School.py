from Team import *



def GenerateHistory():
    return {}

def GenerateStats():
    return {}

def GenerateBoosters():
    return []
def GenerateSchedule():
    return []

class School:

    def __init__(self, team, coach):
        self.team = team
        self.coach = coach
        self.history = GenerateHistory()
        self.rival = "Michigan"
        self.level = 50
        self.prestige = 5
        self.stats = GenerateStats()
        self.location = "East Lansing, MI"
        self.boosters = []
        self.schedule = []
        self.conference = "Big Ten"