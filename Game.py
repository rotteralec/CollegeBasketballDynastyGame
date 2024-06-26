import random




class Game:


    def __init__(self, home, away, NF):
        self.id = 0
        self.home = home
        self.away = away
        #self.date = date #not real date probably 0-42 or whatever total games would be (could be index in season schedule)
        self.NF = NF
        self.homescore = 0
        self.awayscore = 0
        self.played = False



    def playGame(self):
        self.homescore = random.randrange(50,85)
        self.awayscore = random.randrange(40,60)
        self.played = True
        if self.homescore >= self.awayscore:
            return self.home
        else:
            return self.away
    
    def getHome(self):
        return self.home
    
    def getAway(self):
        return self.away
    
    def getHomeScore(self):
        return self.homescore
    def getAwayScore(self):
        return self.awayscore
    

    def getHomeName(self):
        f = open("Schools.csv", "r")
        teams = f.readlines()
        tN = teams[self.home]
        tN = tN.split(",")
        t = tN[1]
        return t
    
    def getAwayName(self):
        f = open("Schools.csv", "r")
        teams = f.readlines()
        tN = teams[self.away]
        tN = tN.split(",")
        t = tN[1]
        return t

        