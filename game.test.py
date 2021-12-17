import unittest
import string

from board import Board
from hangmangame import HangmanGame


class GameTest(unittest.TestCase):

    def setUp(self):
        self.words = get_word()
        self.games = HangmanGame(self.words)
        self.board = Board(self.games)

    def test_start_game(self):
        self.assertEqual(self.words, self.games.words)
        self.games.start()

    def test_guest_win(self):
        self.games.start()
        for item in self.games.target:
            if self.games.credits > 0:
                self.games.quiz(item)

        self.assertTrue(self.games.verify_won())
        self.assertFalse(self.games.verify_defeat())

    def test_guest_not_win(self):
        self.games.start()
        for item in string.ascii_lowercase:
            if self.games.credits > 0:
                self.games.quiz(item)
        self.assertFalse(self.games.verify_won())
        self.assertTrue(self.games.verify_defeat())


def get_word() -> list:
    words: list = []
    with open('palavras.txt', 'r') as file:
        [words.append(item.rstrip()) for item in file]
    return words


if __name__ == '__main__':
    unittest.main()
