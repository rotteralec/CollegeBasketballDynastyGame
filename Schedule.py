import random





class Schedule:

    def __init__(self, year):
        self.year = year
        self.games = []*30



newsched = Schedule(2019)
print(len(newsched.games))