import random

statcat = ["midshooting", "postscoring", "deepthreeshooting","threeptshooting","speed","strength","interiordefense","perimeterdefense","steal","block","offrb","defrb","passing","FT Shooting"]


def generateHT(pos):
    match pos:
        case "PG":
            ht = random.randrange(68,78)
        case "SG":
            ht = random.randrange(70,79)
        case "SF":
            ht = random.randrange(70,81)
        case "PF":
            ht = random.randrange(72,83)
        case "C":
            ht = random.randrange(74,88)
    return ht

def generateWT(pos):
    match pos:
        case "PG":
            wt = random.randrange(175,230)
        case "SG":
            wt = random.randrange(185,240)
        case "SF":
            wt = random.randrange(195,255)
        case "PF":
            wt = random.randrange(200,275)
        case "C":
            wt = random.randrange(220,300)
    return wt




def generateStats(pos, ht, wt):
    statsDict = {}
    overall = 0
    statsDict["Overall"] = overall
    statsDict["midshooting"] = random.randrange(20,100)
    overall = overall + statsDict["midshooting"]
    statsDict["postscoring"] = random.randrange(20,100)
    overall = overall + statsDict["postscoring"]
    statsDict["deepthreeshooting"] = random.randrange(20,100)
    overall = overall + statsDict["deepthreeshooting"]
    statsDict["threeptshooting"] = random.randrange(20,100)
    overall = overall + statsDict["threeptshooting"]
    statsDict["speed"] = random.randrange(20,100)
    overall = overall + statsDict["speed"]
    statsDict["strength"] = random.randrange(20,100)
    overall = overall + statsDict["strength"]
    statsDict["interiordefense"] = random.randrange(20,100)
    overall = overall + statsDict["interiordefense"]
    statsDict["perimeterdefense"] = random.randrange(20,100)
    overall = overall + statsDict["perimeterdefense"]
    statsDict["steal"] = random.randrange(20,100)
    overall = overall + statsDict["steal"]
    statsDict["block"] = random.randrange(20,100)
    overall = overall + statsDict["block"]
    statsDict["offrb"] = random.randrange(20,100)
    overall = overall + statsDict["offrb"]
    statsDict["defrb"] = random.randrange(20,100)
    overall = overall + statsDict["defrb"]
    statsDict["passing"] = random.randrange(20,100)
    overall = overall + statsDict["passing"]
    statsDict["FT Shooting"] = random.randrange(20,100)
    overall = overall + statsDict["FT Shooting"]
    overall = overall / 14
    return statsDict




def generateFirstName():
    ##First name 1387 lines

    firstInd = random.randrange(1,1387)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    firstName = names[firstInd]
    firstName = firstName.split(",")
    f.close()
    return firstName[0].strip()

def generateLastName():
        ##Last name 2671
    lastInd = random.randrange(1,2671)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    lastName = names[lastInd]
    lastName = lastName.split(",")
    f.close()
    return lastName[1].strip()
def generateType(pos, wt, ht):
    types = []
    match pos:
        case "PG":
            ##playmaking ballhandler, scoring ball handler, lockdown d, non - defender, sharpshooter
            if ht >76:
                if wt > 215:
                    types.append("athlete")
            if ht<71:
                if wt<180:
                    types.append("non-defender")
                    types.append("scoring ball handler")
                if wt>215:
                    types.append("playmaking ballhandler")
            if(bool(random.getrandbits(1))):
                types.append("sharpshooter")
        case "SG":
            ##sharpshooter, secondary ball handler, non - defender
            if(bool(random.getrandbits(1))):
                types.append("sharpshooter")
        case "SF":
            ##3 and d, athlete, slashing wing, lock down wing, dynamic shooting wing, spot up shooting wing, playmaking wing
            if(bool(random.getrandbits(1))):
                types.append("sharpshooter")
        case "PF":
            ##stretch 4, lob man, athlete, d rb man, blocker, non - defender
            if(bool(random.getrandbits(1))):
                types.append("sharpshooter")
        case "C":
            ##shot blocker, rim runner, lob man, playmaking big, stretch5, d rb man, non defender
            if(bool(random.getrandbits(1))):
                types.append("sharpshooter")
            if(bool(random.getrandbits(1))):
                types.append("Shot Blocker")
            if(bool(random.getrandbits(1))):
                types.append("playmaking")
    return types


def genYear():
    tYear = [0,1,2,3,4,5,6,7]
    ret = 0
    ret = random.choices(tYear, weights=(10,10,10,10,10,10,10,10),k=1)[0]

    return ret






class Player:
    def __init__(self,id,pos):
        self.id = id
        self.fname = generateFirstName()
        self.lname = generateLastName()
        self.pos = pos
        self.year = genYear() ##evens are non redshirt 0,2,4,6 f,s,j,s odds are redshirt rsf,rss,rsj,rss
        self.ht = generateHT(pos)
        self.length = 3
        self.wt = generateWT(pos)
        self.stats = generateStats(pos, self.ht, self.wt)
        #self.type = generateType()
        self.overall = 0
        self.offense = 0
        self.defense = 0
        

    def trainPlayer(self):
        for i in self.stats.values():
            i += random.randrange(1,5)

    def calcOverall(self):
        tOvr = 0
        tOff = 0
        tDef = 0

        match(self.pos):
            case "PG":
                ###handling, passing, steal, permiter defense, speed, ft shooting, rebounding
                ##--high weight, 
                tOff += self.stats["passing"]*0.20
                tOff += self.stats["FT Shooting"]*0.10
                tOff += self.stats["threeptshooting"]*0.12
                tOff += self.stats["deepthreeshooting"]*0.1
                tOff += self.stats["midshooting"]*0.12
                tOff += self.stats["postscoring"]*0.07
                tOff += self.stats["speed"]*0.15
                tOff += self.stats["strength"]*0.09
                tOff += self.stats["offrb"]*0.05

                tDef += self.stats["defrb"]*0.06
                tDef += self.stats["block"]*0.07
                tDef += self.stats["perimeterdefense"]*0.25
                tDef += self.stats["interiordefense"]*0.07
                tDef += self.stats["steal"]*0.25
                tDef += self.stats["speed"]*0.15
                tDef += self.stats["strength"]*0.15

                tOvr = (tDef + tOff)/2
            case "SG":
                tOff += self.stats["passing"]*0.1
                tOff += self.stats["FT Shooting"]*0.12
                tOff += self.stats["threeptshooting"]*0.15
                tOff += self.stats["deepthreeshooting"]*0.12
                tOff += self.stats["midshooting"]*0.12
                tOff += self.stats["postscoring"]*0.08
                tOff += self.stats["speed"]*0.11
                tOff += self.stats["strength"]*0.1
                tOff += self.stats["offrb"]*0.1

                tDef += self.stats["defrb"]*0.1
                tDef += self.stats["block"]*0.1
                tDef += self.stats["perimeterdefense"]*0.20
                tDef += self.stats["interiordefense"]*0.10
                tDef += self.stats["steal"]*0.20
                tDef += self.stats["speed"]*0.15
                tDef += self.stats["strength"]*0.15

                tOvr = (tDef + tOff)/2
            case "SF":
                
                tOff += self.stats["passing"]*0.12
                tOff += self.stats["FT Shooting"]*0.10
                tOff += self.stats["threeptshooting"]*0.10
                tOff += self.stats["deepthreeshooting"]*0.05
                tOff += self.stats["midshooting"]*0.15
                tOff += self.stats["postscoring"]*0.13
                tOff += self.stats["speed"]*0.10
                tOff += self.stats["strength"]*0.15
                tOff += self.stats["offrb"]*0.10

                tDef += self.stats["defrb"]*0.15
                tDef += self.stats["block"]*0.15
                tDef += self.stats["perimeterdefense"]*0.15
                tDef += self.stats["interiordefense"]*0.15
                tDef += self.stats["steal"]*0.10
                tDef += self.stats["speed"]*0.15
                tDef += self.stats["strength"]*0.15

                tOvr = (tDef + tOff)/2
            case "PF":
                tOff += self.stats["passing"]*0.12
                tOff += self.stats["FT Shooting"]*0.10
                tOff += self.stats["threeptshooting"]*0.10
                tOff += self.stats["deepthreeshooting"]*0.02
                tOff += self.stats["midshooting"]*0.17
                tOff += self.stats["postscoring"]*0.15
                tOff += self.stats["speed"]*0.05
                tOff += self.stats["strength"]*0.14
                tOff += self.stats["offrb"]*0.15

                tDef += self.stats["defrb"]*0.18
                tDef += self.stats["block"]*0.18
                tDef += self.stats["perimeterdefense"]*0.10
                tDef += self.stats["interiordefense"]*0.20
                tDef += self.stats["steal"]*0.11
                tDef += self.stats["speed"]*0.05
                tDef += self.stats["strength"]*0.18

                tOvr = (tDef + tOff)/2
            case "C":
                ## NEED TO CHANGE
                tOff += self.stats["passing"]*0.12
                tOff += self.stats["FT Shooting"]*0.10
                tOff += self.stats["threeptshooting"]*0.08
                tOff += self.stats["deepthreeshooting"]*0.01
                tOff += self.stats["midshooting"]*0.13
                tOff += self.stats["postscoring"]*0.19
                tOff += self.stats["speed"]*0.03
                tOff += self.stats["strength"]*0.15
                tOff += self.stats["offrb"]*0.19

                tDef += self.stats["defrb"]*0.20
                tDef += self.stats["block"]*0.20
                tDef += self.stats["perimeterdefense"]*0.05
                tDef += self.stats["interiordefense"]*0.20
                tDef += self.stats["steal"]*0.10
                tDef += self.stats["speed"]*0.05
                tDef += self.stats["strength"]*0.20

                tOvr = (tDef + tOff)/2
        self.overall = tOvr
        self.offense = tOff
        self.defense = tDef

    def reLoad(self, fname, lname, pos, year, ht, length, wt, overall, stats):
        self.fname = fname
        self.lname = lname
        self.pos = pos
        self.year = year
        self.ht = ht
        self.length = length
        self.wt = wt
        self.overall = overall
        self.stats = stats


        
