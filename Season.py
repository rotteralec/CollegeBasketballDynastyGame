import json
import random


##Seasons recruiting class (Starting with only seniors then look at expanding to juco/transfers at end of year and multi year recruiting)

##15 weeks 30 regular season games or just 30 sections?
#Conference is one more week or up to 5 or 6 with new schools
#national tournament 6 games (or nit/cbi maybe???)
##Offseason: Players leaving, Players transferring, Draft, Offseason recruiting 1 2 3

noncon = []
con = []
confTour = []
natTour = []


##gameday [game, HC RAL, OC RAL, DC RAL, Depth chart, Gameplan, practice]
def genGameday(_game):
    temp_arr = []
    temp_arr.append(_game)
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


    def __init__(self, _season):
        self.season = _season
        self.timeFrame = 0
        self.Gameday = genGameday(_season[0])
        self.Offseason = genOffseason()
    

    def advanceOffSeason(self):
        if self.Offseason[0] is "Draft?":
            ##Covince players to not go to draft 
            self.Offseason.pop()
            return "Draft?"
        if self.Offseason[0] is "Draft":
            return "Draft"

        if self.Offseason[0] is "Transfer":
            return "Transfer"
        
        elif self.Offseason[0][0] is 1:
            return "Recruiting"



    def advanceSeason(self):
        #start with 0 in season and then go from there
        self.timeFrame += 1
        if self.timeFrame < 30:
            self.Gameday = genGameday(self.season[self.timeFrame])
        if self.timeFrame >= 30:
            OffSeason = self.advanceOffSeason()
        if self.timeFrame >= 36:
            #advance season


