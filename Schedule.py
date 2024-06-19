import random
from Game import *
    #Big ten numbers: 121, 173, 174, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228





def genNonCon():
    ##Need to exclude conference opponents (maybe run after and check if in conf schedule then rerun if so)
    tSched = []
    for i in range(0,9):
        newGame = Game(174,random.randrange(0,361),i,0)
        tSched.append(newGame)
    return tSched


def genCon(conf):
    ##16 games in big ten
    ##15 weeks, 2 games a week
    temp = []
    match conf:
        case "Big Ten":
            for i in range(0,23):
                newGame = Game(174, 173, 1, 0)
                temp.append(newGame)
    return temp


def genSched(conf):
    sched = []
    con = genCon("Big Ten")
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
