import random
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
    statsDict["midshooting"] = random.randrange(0,100)
    statsDict["postscoring"] = random.randrange(0,100)
    statsDict["deepthreeshooting"] = random.randrange(0,100)
    statsDict["threeptshooting"] = random.randrange(0,100)
    statsDict["speed"] = random.randrange(0,100)
    statsDict["strength"] = random.randrange(0,100)
    statsDict["interiordefense"] = random.randrange(0,100)
    statsDict["postscoring"] = random.randrange(0,100)
    statsDict["perimeterdefense"] = random.randrange(0,100)
    statsDict["steal"] = random.randrange(0,100)
    statsDict["block"] = random.randrange(0,100)
    statsDict["offrb"] = random.randrange(0,100)
    statsDict["defrb"] = random.randrange(0,100)
    statsDict["passing"] = random.randrange(0,100)
    return statsDict

def generateFirstName():
    ##First name 1387 lines

    print("Generate Player initiated")
    firstInd = random.randrange(1,1387)
    print(firstInd)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    firstName = names[firstInd]
    firstName = firstName.split(",")
    print(firstName[0])
    f.close()
    return firstName[0]

def generateLastName():
        ##Last name 2671
    lastInd = random.randrange(1,2671)
    f = open("NBA-playerlist.csv", "r")
    names = f.readlines()
    lastName = names[lastInd]
    lastName = lastName.split(",")
    print(lastName[1])
    f.close()
    return lastName[1]
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

class Player:
    def __init__(self,pos):
        self.id = 0
        self.fname = generateFirstName()
        self.lname = generateLastName()
        self.pos = pos
        self.ht = generateHT
        self.length = 3
        self.wt = generateWT(self.pos)
        #self.type = generateType()
        self.stats = []
        
