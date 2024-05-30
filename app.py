from Objects import *
from Player import *
from Team import *

global myRoster
myRoster = []


def GeneratePlayer(pos):
    newPlayer = Player(pos)
    print(newPlayer.ht)
    myRoster.append(newPlayer)

def GenerateRoster():
    GeneratePlayer("PG")
    GeneratePlayer("SG")
    GeneratePlayer("SF")
    GeneratePlayer("PF")
    GeneratePlayer("C")
    GeneratePlayer("PG")
    GeneratePlayer("SG")
    GeneratePlayer("SF")
    GeneratePlayer("PF")
    GeneratePlayer("C")
    GeneratePlayer("SG")
    GeneratePlayer("PF")
    GeneratePlayer("C")
    newTeam = Team("Spartans", myRoster, [])

GenerateRoster()




print()