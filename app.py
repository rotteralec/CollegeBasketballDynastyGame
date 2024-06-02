from Objects import *
from Player import *
from Team import *
from DynastyGenerator import *
from Game import *
import json
##174 id is msu in Schools.csv
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
    return newTeam

def adjustRecord(_game):
    if (_game.homescore > _game.awayscore):
        _game.home.wins += 1
        _game.away.losses += 1
    if (_game.homescore < _game.awayscore):
        _game.away.wins += 1
        _game.home.losses += 1
    return

def runSeason(team1, team2):
    for i in range(16):
        newGame = Game(myTeam, rivalTeam, i, 0)
        newGame.playGame()
        adjustRecord(newGame)
        newGame2 = Game(rivalTeam, myTeam, i, 0)
        newGame.playGame()
        adjustRecord(newGame)


    

myTeam = GenerateRoster()
rivalTeam = rosterGen()

runSeason(myTeam,rivalTeam)






print()