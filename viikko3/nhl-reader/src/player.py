class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def __str__(self):
        all = self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
        return all
