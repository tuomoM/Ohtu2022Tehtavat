import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    def test_search_finds(self):
        answer = self.statistics.search("Kurri")
        print(answer)
        self.assertEqual(answer,Player("Kurri",   "EDM", 37, 53))
    def test_search_player_not_found(self):
          answer = self.statistics.search("Laine")
          self.assertEqual(answer,None)
    def test_team_filter_works(self):
        correct = [ Player("Semenko", "EDM", 4, 12),Player("Kurri",   "EDM", 37, 53),Player("Gretzky", "EDM", 35, 89)]
        answer = self.statistics.team("EDM")
        self.assertEqual(answer,correct)
    def test_find_top3_scorers(self):
        correct = [Player("Gretzky", "EDM", 35, 89),Player("Lemieux", "PIT", 45, 54),Player("Yzerman", "DET", 42, 56)]
        answer = self.statistics.top_scorers(2)
        self.assertEqual(answer,correct)
                
        
