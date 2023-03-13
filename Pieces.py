from enum import Enum


class PieceType(Enum):
    """
    Declares the piece type enum.
    - Pawn: 1
    - Knight: 2
    - Bishop: 3
    - Rook: 4
    - Queen: 5
    - King: 6
    """
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class Piece:

    def __init__(self, pieceType : Enum, location : str, white : bool) -> None:
        """
        Creates a piece.
        - piece: PieceType enum for the given piece
        - location: Location of the piece, stored in chess syntax. i.e. A1, E4, ...
        - white: True if white piece, False if black piece
        """
        self.piece = pieceType
        self.location = location
        self.white = white

    
    def chessLocationToCoordinates(self):
        """
        Returns a touple of the 2d array coordinates (x,y) based on pieces chess style location
        """
        return (ord(self.location[0]) - 65, 8 - int(self.location[1]))
    

    def coordinatesToChessLocation(x : int, y : int):
        """
        Returns chess location based on inputted x and y coordinates
        """
        return str(chr(x + 65)) + str(y)
    

    def canMoveTo(self):
        """
        Where a piece can move to. Implement in each subclass.
        """
        raise NotImplemented
    

    def move(self, newX : int, newY : int):
        """
        Move the piece to new location
        """
        self.location = Piece.coordinatesToChessLocation(newX, newY)