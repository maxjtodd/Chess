from enum import Enum


class PieceType(Enum):
    """
    Declares the piece type enum. Pawn: 1, Knight: 2, Bishop: 3, Rook: 4, Queen: 5, King: 6. 
    Number is positive if it's a white piece and is negative if it's a black piece.
    - WHITEPAWN
    - WHITEKNIGHT
    - WHITEBISHOP
    - WHITEROOK
    - WHITEQUEEN
    - WHITEKING
    - BLACKPAWN
    - BLACKKNIGHT
    - BLACKBISHOP
    - BLACKROOK
    - BLACKQUEEN
    - BLACKKING
    """
    WHITEPAWN = 1
    WHITEKNIGHT = 2
    WHITEBISHOP = 3
    WHITEROOK = 4
    WHITEQUEEN = 5
    WHITEKING = 6
    BLACKPAWN = -1
    BLACKKNIGHT = -2
    BLACKBISHOP = -3
    BLACKROOK = -4
    BLACKQUEEN = -5
    BLACKKING = -6



class Piece:

    def __init__(self, pieceType : Enum, location : str, white : bool) -> None:
        """
        Creates a piece.
        - piece: PieceType enum for the given piece
        - location: Location of the piece, stored in chess syntax. i.e. A1, E4, ...
        """
        self.piece = pieceType
        self.location = location

    
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
    

    