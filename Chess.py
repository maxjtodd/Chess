from Pieces import *

class Chess:

    BOARD_SIZE = 8

    def __init__(self) -> None:
        
        self.board = Chess.initializeGame()


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


c = Chess()
c.printBoard()