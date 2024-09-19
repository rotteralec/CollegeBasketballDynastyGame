##This file will generate a new save file with all the schools rosters and recruits

from Team import *
from Player import *
import json
import os
from Recruit import *
from Season import *
#ideas for whats needed in the save file 
#your school id
#roster
#   Player ids
#recruits
# each teams schedule of score/

global Roster
Roster = []
bten = [174, 173, 121, 162, 222, 231, 251, 241, 117, 217, 355, 124, 177, 345, 192, 279, 323, 228]
global conf 
conf = {}
global playerCount



def genSeason():
    newSeason = Season()
    return newSeason

def genBlankSeason():
    #30 games, 10 noncon, 20 con
    tGame =  [0,0,0,0,0,0,False]
    tList = [tGame]*30
    return tList


def saveSchedule(_sched):
    with open("saveSched.json", "w") as outfile:
        json.dump(_sched, outfile)
    return 1


##TO DO NEXT GENERATE EMPTY SCHEDULE FOR EACH TEAM, then add versus games in corr. sched when creating your own
def genSchedule():
    tSched = {}
    for i in range(362):
        tSched[i] = genBlankSeason()
    saveSchedule(tSched)

def GeneratePlayer(id, pos):
    newPlayer = Player(id, pos)
    newPlayer.calcOverall()
    Roster.append(newPlayer)

def loadTeam(id, name, roster, recruits=[]):
    return Team(id, name, roster,recruits)

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

                
#def toMyRoster(ros):

def genRecruit(_id, _pos):
    tRecruit = Recruit(_id, _pos)
    tRecruit.getPlayer().calcOverall()
    return tRecruit




def genClass():
    tClass = []
    tClass.append(genRecruit(0, "PG"))
    tClass.append(genRecruit(1, "SG"))
    tClass.append(genRecruit(2, "SF"))
    tClass.append(genRecruit(3, "PF"))
    tClass.append(genRecruit(4, "C"))
    tClass.append(genRecruit(5, "PG"))
    tClass.append(genRecruit(6, "SG"))
    tClass.append(genRecruit(7, "SF"))
    tClass.append(genRecruit(8, "PF"))
    tClass.append(genRecruit(9, "C"))
    tClass.append(genRecruit(10, "SG"))
    tClass.append(genRecruit(11, "PF"))
    tClass.append(genRecruit(12, "C"))
    return tClass



def unpackRecruit(_recruit):
    tDict = {}
    tPlayer = unpackPlayer(_recruit.getPlayer())
    tDict = {"priorities": _recruit.priorities, "player": tPlayer, "schools": _recruit.schools, "hs": _recruit.hs, "location": _recruit.location, "id": _recruit.id}
    return tDict

def loadRecruit(_dict, _id):
    tRecruit = Recruit(_id, _dict["player"]["pos"])
    tRecruit.overrideSelf(_dict["priorities"], _dict["schools"], _dict["location"], _dict["id"])
    return tRecruit
    

def readRecruit(_id):
    with open("saveRecruit.json", "r") as openfile:
        tDict = json.load(openfile)
        return loadRecruit(tDict[str(_id)], _id)
    
def readRecruits():
    tArr = []
    with open("saveRecruit.json", "r") as openfile:
        tDict = json.load(openfile)
        for i in range(len(tDict)):
            tArr.append(loadRecruit(tDict[str(i)],i))
    return tArr


def saveRecruits(_recruits):
    tDict = {}
    with open("saveRecruit.json", "w") as outfile:
        for i in _recruits:
            tDict[i.id] = unpackRecruit(i)
        json.dump(tDict, outfile)
        
def unpackPlayer(_player):
    tDict = {}
    tDict = {"fname":_player.fname, "lname": _player.lname, "pos": _player.pos, "year": _player.year, "ht": _player.ht, "ln": _player.length, "wt": _player.wt, "overall": _player.overall, "stats": _player.stats, "offense": _player.offense, "defense": _player.defense}
    return tDict

def loadPlayer(_id, _player):
    tPlayer = Player(_id, _player["pos"])
    tPlayer.reLoad(_player["fname"], _player["lname"], _player["pos"], _player["year"], _player["ht"], _player["ln"], _player["wt"], _player["overall"], _player["stats"], _player["offense"], _player["defense"])
    return tPlayer

def saveRoster(rost):
    tDict = {}
    teamDict = {}
    with open("testsave.json", "w") as outfile:
        for i in rost.roster:
            tDict[i.id] = unpackPlayer(i)
        conf[rost.id] = tDict
        json.dump(conf, outfile)

def readSave(file):
    with open("testsave.json", "r") as openfile:
        return json.load(openfile)

def resetSave(file):
    open(file, 'w').close()

def saveSeason(_season):
    sched = {}
    with open("saveSched.json", "w") as outfile:
    
        sched[_season.teamID] = {"schedule": serializeSeason(_season.schedule), "timeFrame": _season.timeFrame, "Gameday": _season.Gameday, "Offseason": _season.Offseason}
        json.dump(sched, outfile)

def serializeSeason(_season):
    tSeason = []
    for i in _season:
        tGame = serializeGame(i)
        tSeason.append(tGame)
    return tSeason

def serializeGame(_game):
    
    return [_game.id, _game.home, _game.away, _game.NF, _game.homescore, _game.awayscore, _game.played]

def readSchedule():
    tDict = {}
    with open("saveSched.json", "r") as openfile:
        tDict = json.load(openfile)
    return tDict['174']

    
def loadSchedule(_sched):    
    tSeason = Season()
    tSeason.loadSeason(_sched['schedule'],_sched['timeFrame'], _sched['Gameday'], _sched['Offseason'], '174')
    return tSeason
