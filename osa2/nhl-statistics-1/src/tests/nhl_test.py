import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_loytaa(self):
        pelaaja = self.stats.search("Kurri")

        self.assertEqual(str(pelaaja), "Kurri EDM 37 + 53 = 90")

    def test_search_ei_loyda(self):
        pelaaja = self.stats.search("Kuurri")
        self.assertEqual(str(pelaaja), "None")
    
    def test_team_loytyy(self):
        team = self.stats.team("PIT")
        self.assertEqual(str(team[0]), "Lemieux PIT 45 + 54 = 99")

    def test_team_ei_loyda(self):
        team = self.stats.team("PIE")
        self.assertEqual(team, list())

    def test_top(self):
        top = self.stats.top(2)

        self.assertEqual(str(top[0]), str(self.stats.search("Gretzky")))
        self.assertEqual(str(top[1]), str(self.stats.search("Lemieux")))
        