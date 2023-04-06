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



    