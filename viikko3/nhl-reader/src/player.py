from unittest.case import _AssertRaisesContext


class Player(object):
    def __init__(self, name,team,assist,goals, nationality):
        self.name = name
        self.team = team
        self.assists = assist
        self.goals = goals
        self.points = goals + assist
        self.nationality = nationality
    def get_nationality(self):
        return self.nationality    
    def get_points(self):
        return self.points   
    def __str__(self):
        return f"{self.name:25}" + f"{self.team:5}" + f"{str(self.assists):3}" +" + "+ f"{str(self.goals):3}" + " = " + str(self.points)
    
    # comparison methods
    def __eq__(self,other):
        return self.points == other.points
    def __lt__(self,other):
        return self.points < other.points
    def __le__(self,other):
        return self.points <= other.points
    def __gt__(self,other):
        return self.points > other.points
    def __ge__(self,other):
        return self.points >= other.points
    
  
