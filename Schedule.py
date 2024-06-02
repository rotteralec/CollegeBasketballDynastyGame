import random
from Game import *
    #Big ten numbers: 121, 173, 174, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228


def genSched(conf):
    sched = []
    genCon("Big Ten")



def genNonCon():
    return

def genCon(conf):
    ##16 games in big ten
    ##15 weeks, 2 games a week
    temp = []
    match conf:
        case "Big Ten":
            for i in range(16):
                newGame = Game(174, 173, 1, 0)
                temp.append(newGame)


    
    return

class Schedule:

    def __init__(self, year):
        self.year = year
        self.games = genSched({"Big Ten"})



newsched = Schedule(2019)
print(newsched.games)