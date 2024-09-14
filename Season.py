import json
import random
from Game import *




##Seasons recruiting class (Starting with only seniors then look at expanding to juco/transfers at end of year and multi year recruiting)


noncon = []
con = []
confTour = []
natTour = []





def genNonCon():
    ##Need to exclude conference opponents (maybe run after and check if in conf schedule then rerun if so)
    tSched = []
    for i in range(0,11):
        newGame = Game(174,random.randrange(0,361),0)
        tSched.append(newGame)
    return tSched


def genCon(conf, mySchoolID):

    temp = []
    match conf:

        case "Big Ten":
            ##20 games in big ten
            ##6 home and aways with 3 teams
            ##7 home with 7 teams
            #7 away with 7 teams
            bten = [174, 173, 121, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228]
            ha = [173, 121, 162]
            away = [222, 231, 251, 241, 117, 217, 355]
            home = [124, 177, 345, 192, 279, 323, 228]
            for i in range(0,3):
                newGame = Game(mySchoolID,ha[i], 0)
                temp.append(newGame)
                newGame = Game(ha[i],mySchoolID, 0)
                temp.append(newGame)
            for i in range(0,7):
                newGame = Game(mySchoolID,home[i],0)
                temp.append(newGame)
                newGame = Game(away[i],mySchoolID,0)
                temp.append(newGame)
    
    random.shuffle(temp)

    return temp


def genSched(conf):
    sched = []
    con = genCon("Big Ten", 174)
    noncon = genNonCon()
    for i in noncon:
        sched.append(i)
    for i in con:
        sched.append(i)
    return sched



##gameday [game, HC RAL, OC RAL, DC RAL, Depth chart, Gameplan, practice]
def genGameday():
    temp_arr = []
    temp_arr.append([])
    temp_arr.append([])
    temp_arr.append([])
    temp_arr.append(False)
    temp_arr.append(False)
    temp_arr.append(False)
    return temp_arr

# [HC RAL, OC RAL, DC RAL] With Transfers
#players leaving for draft?
#1 draft
#players transferring
#3 offseason recruiting sections with transfers (start after draft for now to make it easier)
def genOffseason():
    tOS = []
    tOS.append("Draft?")
    tOS.append("Draft")
    tOS.append("Transfer?")
    tOS.append([1])
    tOS.append([2])
    tOS.append([3])
    return tOS

class Season:


    def __init__(self):
        self.schedule = genSched("Big Ten")
        self.timeFrame = 0
        self.Gameday = genGameday()
        self.Offseason = genOffseason()
        self.teamID = 174
    
    def loadSeason(self, schedule, timeFrame, Gameday, Offseason, teamID):
        self.schedule = schedule
        self.timeFrame = timeFrame
        self.Gameday = Gameday
        self.Offseason = Offseason
        return
    def advanceOffSeason(self):
        if self.Offseason[0] == "Draft?":
            ##Covince players to not go to draft 
            self.Offseason.pop()
            return "Draft?"
        if self.Offseason[0] == "Draft":
            self.Offseason.pop()
            return "Draft"

        if self.Offseason[0] == "Transfer":
            self.Offseason.pop()
            return "Transfer"
        
        elif self.Offseason[0][0] == 1:
            self.Offseason.pop()
            return "Recruiting 1"
        
        elif self.Offseason[0][0] == 2:
            self.Offseason.pop()
            return "Recruiting 2"
        
        elif self.OffSeason[0][0] == 3:
            self.Offseason.pop()
            return "Recruiting 3"

    def newSeason(self):
        #need to archive current season and build new one
        return

    def getCurrentGame(self):

        return self.schedule[self.timeFrame]
    
    def getScheduleGame(self, _int):
        return self.schedule[_int]

    def getTimeFrame(self):
        return self.timeFrame

    def advanceSeason(self):

        winner = self.schedule[self.timeFrame].playGame()
        print(self.timeFrame)

        #start with 0 in season and then go from there
        self.timeFrame += 1
        if self.timeFrame < 30:
            self.Gameday = genGameday()
        if self.timeFrame >= 30:
            OffSeason = self.advanceOffSeason()
        if self.timeFrame >= 36:
            #advance season
            self.newSeason()


