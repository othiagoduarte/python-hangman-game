import random

class HangmanGame:

    def __init__(self, words: list):
        self.credits: int = 6
        self.target: str = None
        self.correctMove: list = []
        self.defeatMove: list = []
        self.words = words

    def start(self):
        self.credits: int = 6
        self.correctMove: list = []
        self.defeatMove: list = []
        self.target = random.choice(self.words)

    def quiz(self, letter: str):
        if self.credits > 0:
            if letter in self.target:
                self.correctMove.append(letter)
            else:
                self.defeatMove.append(letter)
                self.credits -= 1

    def verify_won(self):
        return len(self.target) == len(self.correctMove)

    def verify_defeat(self):
        return self.credits <= 0
