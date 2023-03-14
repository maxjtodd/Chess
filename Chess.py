from Pieces import *

class Chess:
    """
    Controls the environment for chess
    """

    BOARD_SIZE = 8

    def __init__(self) -> None:
        """
        Creates the initial state of the chess game
        - board: 2d array with 0's as empty space and piece values according to PieceType enum
        - whiteTurn: True if the turn is white, false if the turn is black
        """
        self.board = Chess.initializeGame()
        self.whiteTurn = True


    def initializeGame():
        """
        Create the iniital state of chess
        - 0 stores empty space
        - Other numbers are stored according to PieceType enum values
        """
        board = [
                    [PieceType.BLACKROOK.value, PieceType.BLACKKNIGHT.value, PieceType.BLACKBISHOP.value, PieceType.BLACKQUEEN.value, PieceType.BLACKKING.value, PieceType.BLACKBISHOP.value, PieceType.BLACKKNIGHT.value, PieceType.BLACKROOK.value],
                    [PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value, PieceType.BLACKPAWN.value],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value, PieceType.WHITEPAWN.value],
                    [PieceType.WHITEROOK.value, PieceType.WHITEKNIGHT.value, PieceType.WHITEBISHOP.value, PieceType.WHITEQUEEN.value, PieceType.WHITEKING.value, PieceType.WHITEBISHOP.value, PieceType.WHITEKNIGHT.value, PieceType.WHITEROOK.value]
                ]
        
        return board
    
    def printBoard(self):
        for row in self.board:
            print(row)

