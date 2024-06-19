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





class Season:


    def __init__(self, _season):
        self.season = _season
        