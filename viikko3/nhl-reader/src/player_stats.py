from player import Player

class PlayerStats:
     def __init__(self,playerReader):
        self.players = playerReader.get_Players()
        self.players.sort(key = lambda x: x.points, reverse = True)
     def top_scorers_by_nationality(self, nationality):
        nations_players = []
        for player in self.players:
             if(player.nationality == nationality):
                 nations_players.append(player)
        return nations_players         
         
        
         
         
         
