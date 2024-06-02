##This file will generate a new save file with all the schools rosters and recruits

from Team import *
from Player import *

#ideas for whats needed in the save file 
#your school id
#roster
#   Player ids
#recruits
# each teams schedule of score/

global Roster
Roster = []
def GeneratePlayer(pos):
    newPlayer = Player(pos)
    print(newPlayer.ht)
    Roster.append(newPlayer)


def rosterGen():
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
    newTeam2 = Team("Wolverines", Roster, [])
    return newTeam2