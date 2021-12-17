from hangmangame import HangmanGame


class Board:

    def __init__(self, game: HangmanGame):
        self.game = game

    def mask_word(self):
        result = ''
        for item in self.game.target:
            if item in self.game.correctMove:
                result += item + ' '
            else:
                result += '_ '
        return result

    def get_score(self):
        return self.game.credits * len(self.game.target) * len(self.game.correctMove) * 100

    def result_game(self):
        if self.game.verify_won():
            return f"""
**********************************************
            You Win
            score: {self.get_score()}     
**********************************************
            """
        else:
            return f""" 
**********************************************
            You lose
            target word: {self.game.target}
            score: {self.get_score()}     
**********************************************
            """

    def get_hangman(self):
        if self.game.credits == 5:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}
 
 |------T
 |      
 |
 |
**********************************************
            """

        if self.game.credits == 5:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |   
 |
**********************************************
            """
        if self.game.credits == 4:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |      | 
 |
 L
**********************************************
            """
        if self.game.credits == 3:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |    / | 
 |
 L
*********************************************
            """
        if self.game.credits == 2:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |    / | |
 |
 L   
**********************************************
            """
        if self.game.credits == 1:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |    / | |
 |     |
 L   
 **********************************************
            """
        if self.game.credits == 0:
            return f"""
**********************************************

 score: {self.get_score()} 
 word target: {self.mask_word()}

 |------T
 |      O
 |    / | |
 |     | | 
 L   
**********************************************
            """