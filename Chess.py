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

        # Keeps track of turns
        self.whiteTurn = True

        # Keeps track of whether or not king is in check
        self.whiteInCheck = False
        self.blackInCheck = False

        # Keeps track of en passent possibilities
        self.twoWhitePawnMovement = set()
        self.twoBlackPawnMovement = set()


    def initializeGame() -> list:
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
    

    def movePiece(self, oldX : int, oldY : int, move : tuple) -> None:
        """
        Moves piece from one position to another. Should only be called when the piece
        is available to be moved to the new position.
        - oldX: old x position of piece to be moved
        - oldY: old y position of piece to be moved
        - move: tuple from function canMoveTo containing information about move
        """

        # Get piece information
        piece = self.board[oldY][oldX]
        self.board[oldY][oldX] = 0

        # Get new movement piece information
        newX = move[0]
        newY = move[1]
        capture = move[2]

        # Check for en passant captures
        enPassant = False

        # Check for white en passant capture
        if piece == PieceType.WHITEPAWN.value and newX in self.twoBlackPawnMovement and self.board[newY][newX] == 0 and capture:

            # En passant occured
            self.board[oldY][newX] = 0
            enPassant = True

        # Check for black en passant capture
        elif piece == PieceType.BLACKPAWN.value and newX in self.twoWhitePawnMovement and self.board[newY][newX] == 0 and capture :

            # En passant occured
            self.board[oldY][newX] = 0
            enPassant = True

        # Move piece
        self.board[newY][newX] = piece


        # TODO Check for check
        check = False

        # TODO Check for promotion
        promotion = False


        # Check for white en passant values
        if piece == PieceType.WHITEPAWN.value and (oldY - newY) == 2:
            self.twoWhitePawnMovement.add(newX)

        # Check for black en passant values
        elif piece == PieceType.BLACKPAWN.value and (newY - oldY) == 2:
            self.twoBlackPawnMovement.add(newX)

        # TODO Check for check

        # Set other player turn
        self.whiteTurn = not self.whiteTurn

        # Return move information in form of (check, promotion, enPassant)
        return (check, promotion, enPassant)

    
    def canMoveTo(self, x : int, y : int) -> list:
        """
        Returns a list of tiles where the piece of the inputted quardinates can move.
        """

        # Get the piece
        piece = self.board[y][x]

        # if piece != 0:
        #     print("Piece is: ", PieceType(piece))
        #     self.printBoard()



        # Set up the movement availability
        # Formatted as touple. (x to move to, y to move to, boolean true if piece capture)
        positions = []

        #
        # TODO En Passant
        # TODO Pawn promotions
        # TODO Castling
        # TODO Check : seperate function, checks squares around the king to determine if attacked
        # 


        # Get the available positions to move
        if piece == 0:
            return None
        
        # White turn, only white can move
        elif self.whiteTurn:
            
            # White pawn movement positions
            if piece ==  PieceType.WHITEPAWN.value:

                # TODO promotions

                # Pawns can move forward once at any time if nothing blocking it's path
                if self.board[y - 1][x] == 0:
                    positions.append((x, y - 1, False))

                # Determine regular capture movements
                potentialPositions = [(x - 1, y - 1), (x + 1, y - 1)]

                for position in potentialPositions:
                    # Determine if capture is in bounds
                    if position[0] >= 0 and position[1] >= 0 and position[0] < Chess.BOARD_SIZE and position[1] < Chess.BOARD_SIZE:

                        # Determine if piece in capture square is black
                        if self.board[position[1]][position[0]] < 0:
                            positions.append((position[0], position[1], True))

                # Determine en passant capture movements

                # Check left en passant
                if (x - 1) in self.twoBlackPawnMovement and y == 3:
                    # Left en passant possible, append as capture
                    positions.append((x - 1, y - 1, True))

                # Check right en passant
                if (x + 1) in self.twoBlackPawnMovement and y == 3:
                    # Right en passant possible, append as capture
                    positions.append((x + 1, y - 1, True))
                

                # Pawns can move forward twice if hasnt moved and nothing blocking it's path
                if y == 6 and self.board[y - 2][x] == 0:
                    positions.append((x, y - 2, False))


            # White Knight movement positions
            elif piece ==  PieceType.WHITEKNIGHT.value:

                # Define positions for knight to move (to add to existing x and y values)
                potentialPositions = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1)]

                # Determine where the knight can move
                for move in potentialPositions:
                    # Move must be in bounds of the board
                    if x + move[0] >= 0 and y + move[1] >= 0 and x + move[0] < Chess.BOARD_SIZE and y + move[1] < Chess.BOARD_SIZE:
                        
                        # Move cannot land on a white piece
                        landingSquare = self.board[y + move[1]][x + move[0]]

                        if landingSquare <= 0:

                            # Knight capturing piece
                            if landingSquare < 0:
                                positions.append((x + move[0], y + move[1], True))
                            # Knight not capturing piece
                            else:
                                positions.append((x + move[0], y + move[1], False))


            # White Bishop movement positions
            elif piece == PieceType.WHITEBISHOP.value:

                # Determine the up right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y - i
                    
                    # Determine if the up right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the up left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y - i
                    
                    # Determine if the up left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the down left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y + i
                    
                    # Determine if the down left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the down right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y + i
                    
                    # Determine if the down right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break


            # White Rook movement positions
            elif piece == PieceType.WHITEROOK.value:

                # Determine left move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x - i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine right move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x + i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine up positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y - i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine down positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y + i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break


            # Whtie Queen movement positions
            elif piece == PieceType.WHITEQUEEN.value:

                # Determine the vertical and horizontal movement positions

                # Determine left move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x - i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine right move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x + i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine up positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y - i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine down positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y + i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if black, stop if white
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a black piece, append and stop, capture
                        elif landingSquare < 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine the diagnal movement positions

                # Determine the up right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y - i
                    
                    # Determine if the up right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the up left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y - i
                    
                    # Determine if the up left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the down left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y + i
                    
                    # Determine if the down left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break

                # Determine the down right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y + i
                    
                    # Determine if the down right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if black then stop, stop if white
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is black square, append and stop going, capture
                    elif landingSquare < 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is white square, no new move and stop going
                    else:
                        break


            # White King movement positions
            elif piece == PieceType.WHITEKING.value:

                # Define all possible king movement positions, relative to current position
                potentialPositions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

                # Determine valid potential positions. 
                for position in potentialPositions:

                    # Determine if move is in bounds
                    newX, newY = (x + position[0]), (y + position[1])

                    if newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Move and append no capture if 0 (empty), Move and append with capture if negative (black piece), don't do anything if white piece
                        landingSquare = self.board[newY][newX]

                        # Empty square, move and append (no capture)
                        if landingSquare == 0:
                            positions.append((newX, newY, False))
                        
                        # Black piece, move and append (capture)
                        elif landingSquare < 0:
                            positions.append((newX, newY, True))


        # Black turn, only black can move
        else:
            
            # Black pawn movement positions
            if piece ==  PieceType.BLACKPAWN.value:

                # TODO promotions

                # Pawns can move forward once at any time if nothing blocking it's path
                if self.board[y + 1][x] == 0:
                    positions.append((x, y + 1, False))

                # Determine regular capture movements
                potentialPositions = [(x - 1, y + 1), (x + 1, y + 1)]

                for position in potentialPositions:
                    # Determine if capture is in bounds
                    if position[0] >= 0 and position[1] >= 0 and position[0] < Chess.BOARD_SIZE and position[1] < Chess.BOARD_SIZE:

                        # Determine if piece in capture square is white
                        if self.board[position[1]][position[0]] > 0:
                            positions.append((position[0], position[1], True))

                # Determine en passant capture movements

                # Check left en passant
                if (x - 1) in self.twoWhitePawnMovement and y == 4:
                    # Left en passant possible, append as capture
                    positions.append((x - 1, y + 1, True))

                # Check right en passant
                if (x + 1) in self.twoWhitePawnMovement and y == 4:
                    # Right en passant possible, append as capture
                    positions.append((x + 1, y + 1, True))

                # Pawns can move forward twice if hasnt moved and nothing blocking it's path
                if y == 1 and self.board[y + 2][x] == 0:
                    positions.append((x, y + 2, False))


            # Black Knight movement positions
            elif piece ==  PieceType.BLACKKNIGHT.value:

                # Define positions for knight to move (to add to existing x and y values)
                potentialPositions = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1)]

                # Determine where the knight can move
                for move in potentialPositions:
                    # Move must be in bounds of the board
                    if x + move[0] >= 0 and y + move[1] >= 0 and x + move[0] < Chess.BOARD_SIZE and y + move[1] < Chess.BOARD_SIZE:
                        
                        # Move cannot land on a black piece
                        landingSquare = self.board[y + move[1]][x + move[0]]

                        if landingSquare >= 0:

                            # Knight capturing piece
                            if landingSquare > 0:
                                positions.append((x + move[0], y + move[1], True))
                            # Knight not capturing piece
                            else:
                                positions.append((x + move[0], y + move[1], False))


            # Black Bishop movement positions
            elif piece == PieceType.BLACKBISHOP.value:

                # Determine the up right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y - i
                    
                    # Determine if the up right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the up left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y - i
                    
                    # Determine if the up left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the down left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y + i
                    
                    # Determine if the down left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the down right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y + i
                    
                    # Determine if the down right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break


            # Black Rook movement positions
            elif piece == PieceType.BLACKROOK.value:

                # Determine left move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x - i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine right move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x + i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break

                # Determine up positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y - i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break

                # Determine down positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y + i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break


            # Black Queen movement positions
            elif piece == PieceType.BLACKQUEEN.value:

                # Determine the vertical and horizontal movement positions

                # Determine left move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x - i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a white piece, no new move and stop going
                        else:
                            break

                # Determine right move positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newX = x + i

                    if newX >= 0 and newX < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[y][newX]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((newX, y, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((newX, y, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break

                # Determine up positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y - i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break

                # Determine down positions
                for i in range(1, 8):

                    # Determine if the movement is in bounds
                    newY = y + i

                    if newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Determine movement options. Append and keep going if square is 0, append and stop if white, stop if black
                        landingSquare = self.board[newY][x]
                        
                        # Square is empty, append and keep going, no capture
                        if landingSquare == 0:
                            positions.append((x, newY, False))

                        # Square has a white piece, append and stop, capture
                        elif landingSquare > 0:
                            positions.append((x, newY, True))
                            break

                        # Square has a black piece, no new move and stop going
                        else:
                            break

                # Determine the diagnal movement positions

                # Determine the up right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y - i
                    
                    # Determine if the up right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the up left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y - i
                    
                    # Determine if the up left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the down left movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x - i
                    newY = y + i
                    
                    # Determine if the down left movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break

                # Determine the down right movement positions
                for i in range(1, 8):

                    # Set up the new x and new y variables
                    newX = x + i
                    newY = y + i
                    
                    # Determine if the down right movement is not in bounds, break loop
                    if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                        break

                    # In bounds, keep adding if sqares are empty. Add if white then stop, stop if black
                    landingSquare = self.board[newY][newX]

                    # Square is empty, append and keep going, no capture
                    if landingSquare == 0:
                        positions.append((newX, newY, False))

                    # Square is white square, append and stop going, capture
                    elif landingSquare > 0:
                        positions.append((newX, newY, True))
                        break

                    # Square is black square, no new move and stop going
                    else:
                        break


            # Black King movement positions
            elif piece == PieceType.BLACKKING.value:

                # Define all possible king movement positions, relative to current position
                potentialPositions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

                # Determine valid potential positions. 
                for position in potentialPositions:

                    # Determine if move is in bounds
                    newX, newY = (x + position[0]), (y + position[1])

                    if newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE:

                        # Move and append no capture if 0 (empty), Move and append with capture if positive (white piece), don't do anything if black piece
                        landingSquare = self.board[newY][newX]

                        # Empty square, move and append (no capture)
                        if landingSquare == 0:
                            positions.append((newX, newY, False))
                        
                        # White piece, move and append (capture)
                        elif landingSquare > 0:
                            positions.append((newX, newY, True))



        # print(positions)
        return positions

        
    def checkCheck(self):
        """
        Determines whether check is given
        """

        # Black turn, check white for check
        


    def printBoard(self):

        for row in self.board:

            for val in row:

                p = ""

                if val == 1:
                    p = "wP"

                elif val == 2:
                    p = "wK"

                elif val == 3:
                    p = "wB"

                elif val == 4:
                    p = "wR"

                elif val == 5:
                    p = "wQ"

                elif val == 6:
                    p = "wO"

                elif val == -1:
                    p = "bP"

                elif val == -2:
                    p = "bK"

                elif val == -3:
                    p = "bB"

                elif val == -4:
                    p = "bR"

                elif val == -5:
                    p = "bQ"

                elif val == -6:
                    p = "bO"

                else:
                    p = "."

                print('{:3s}'.format(p), end='   ')

            print("\n")

        print("-------------------------------------------")


