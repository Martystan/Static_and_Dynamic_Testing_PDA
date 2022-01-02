import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("diamond", 1)
        self.card2 = Card("spade", 10)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()

    def test_can_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_can_return_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_can_return_total(self):
        self.assertEqual("You have a total of11",self.card_game.cards_total(self.cards))