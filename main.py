from board import Board
from hangmangame import HangmanGame


def get_word() -> list:
    words: list = []
    with open('palavras.txt', 'r') as file:
        [words.append(item.rstrip()) for item in file]
    return words


if __name__ == '__main__':
    print("*********** Hangman's Game ********")
    game = HangmanGame(get_word())
    game.start()
    board = Board(game)
    print(board.get_hangman())
    while True:
        game.quiz(input("Digita uma letra:"))
        print(board.get_hangman())
        if game.verify_won() or game.verify_defeat():
            print(board.result_game())
            break
