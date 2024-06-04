from Objects import *
from Player import *
from Team import *
from DynastyGenerator import *
from Game import *
import json
##174 id is msu in Schools.csv
global myRoster
myRoster = []
global standings
standings = {}


def updateStandings():
    prevWin = 0
"""     for i in standings:
        if i.wins > prev  """



def adjustRecord(_game):
    if (_game.homescore > _game.awayscore):
        _game.home.wins += 1
        _game.away.losses += 1
    if (_game.homescore < _game.awayscore):
        _game.away.wins += 1
        _game.home.losses += 1

    #need to update standings
    return

def runSeason(team1, team2):
    for i in range(16):
        newGame = Game(team1, team2, i, 0)
        newGame.playGame()
        adjustRecord(newGame)
        newGame2 = Game(team2, team1, i, 0)
        newGame.playGame()
        adjustRecord(newGame)


    
resetSave("testsave.json")

myRosterID = genConference("Big Ten")
myConf = readRoster("testsave.json")
print(myConf[str(121)])

