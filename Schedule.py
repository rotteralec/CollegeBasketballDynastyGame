import random
from Game import *
    #Big ten numbers: 174, 173, 121, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228
bten = [174, 173, 121, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228]
ha = [173, 121, 162]
away = [222, 231, 251, 241, 117, 217, 355]
home = [124, 177, 345, 192, 279, 323, 228]




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
    if temp != []:
        random.shuffle(temp)

    return temp


def genSched(conf):
    sched = []
    con = genCon("Big Ten", 174)
    noncon = genNonCon()
    for i in con:
        sched.append(i)
    for i in noncon:
        sched.append(i)
    return sched
    

class Schedule:

    def __init__(self, year):
        self.year = year
        self.games = genSched({"Big Ten"})

sched = Schedule(2018)

for i in sched.games:
    print(i.home)
