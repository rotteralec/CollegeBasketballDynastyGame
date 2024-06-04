##This file will generate a new save file with all the schools rosters and recruits

from Team import *
from Player import *
import json
import os
#ideas for whats needed in the save file 
#your school id
#roster
#   Player ids
#recruits
# each teams schedule of score/

global Roster
Roster = []
bten = [121, 173, 174, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228]
global conf 
conf = {}

def GeneratePlayer(id, pos):
    newPlayer = Player(id, pos)
    newPlayer.calcOverall()
    Roster.append(newPlayer)








def rosterGen(id, name):
    GeneratePlayer(0, "PG")
    GeneratePlayer(1, "SG")
    GeneratePlayer(2, "SF")
    GeneratePlayer(3, "PF")
    GeneratePlayer(4, "C")
    GeneratePlayer(5, "PG")
    GeneratePlayer(6, "SG")
    GeneratePlayer(7, "SF")
    GeneratePlayer(8, "PF")
    GeneratePlayer(9, "C")
    GeneratePlayer(10, "SG")
    GeneratePlayer(11, "PF")
    GeneratePlayer(12, "C")
    newTeam2 = Team(id, name, Roster, [])
    return newTeam2

def grabSchoolInfo(id):
    with open("schools.csv", "r") as infile:
        openFile = infile.readlines()
        return(openFile[id])


def genConference(conf):
    #Big ten numbers: 121, 173, 174, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228
    ##will generate all teams and roster for conference
    match conf:
        case "Big Ten":
            for i in bten:
                schoolInfo = grabSchoolInfo(i)
                schoolInfo = schoolInfo.split(",")
                newTeam = rosterGen(int(i), schoolInfo[1])
                saveRoster(newTeam)
            return 174

                




def unpackPlayer(_player):
    tDict = {}
    tDict = {"fname":_player.fname, "lname": _player.lname, "pos": _player.pos, "ht": _player.ht, "ln": _player.length, "wt": _player.wt, "overall": _player.overall, "stats": _player.stats}
    return tDict


def saveRoster(rost):
    tDict = {}
    teamDict = {}
#"""     if (os.path.getsize("C:/Users/rotte/CollegeBasketballDynastyGame/testsave.json") > 0):
   #     return 0
  #  else: """
    with open("testsave.json", "w") as outfile:
        for i in rost.roster:
            tDict[i.id] = unpackPlayer(i)
        conf[rost.id] = tDict
        json.dump(conf, outfile)

def readRoster(file):
    with open("testsave.json", "r") as openfile:
        return json.load(openfile)

def resetSave(file):
    open(file, 'w').close()