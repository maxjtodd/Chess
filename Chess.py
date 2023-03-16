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

        # TODO: remove line under
        # self.board[4][2] = 1
        #self.board[4][5] = 2

        self.whiteTurn = True


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
    

    def movePiece(self, oldX : int, oldY : int, newX : int, newY : int) -> None:
        """
        Moves piece from one position to another. Should only be called when the piece
        is available to be moved to the new position.
        """

        # Move piece
        piece = self.board[oldY][oldX]
        self.board[oldY][oldX] = 0
        self.board[newY][newX] = piece

    
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
        # TODO capture
        # 

        # Get the available positions to move
        if piece == 0:
            return None
        
        # White pawn movement positions
        elif piece ==  PieceType.WHITEPAWN.value:

            # TODO promotions
            # TODO capture

            # Pawns can move forward once at any time
            positions.append((x, y - 1, False))

            # Pawns can move forward twice if hasnt moved
            if y == 6:
                positions.append((x, y - 2, False))
        

        # Black pawn movement positions
        elif piece ==  PieceType.BLACKPAWN.value:

            # TODO promotions
            # TODO capture

            # Pawns can move forward once at any time
            positions.append((x, y + 1, False))

            # Pawns can move forward twice if hasnt moved
            if y == 1:
                positions.append((x, y + 2, False))


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
                            

        # White Bishop movement positions
        elif piece == PieceType.WHITEBISHOP.value:

            # Determine the up right movement positions
            for i in range(1, 8):

                # Set up the new x and new y variables
                newX = x + i
                newY = y - i
                
                # Determine if the up right movement is not in bounds, break loop
                if not(newX >= 0 and newX < Chess.BOARD_SIZE and newY >= 0 and newY < Chess.BOARD_SIZE):
                    print((x + i), ", ", (y - i), "  not in bounds")
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
                    print((x + i), ", ", (y - i), "  not in bounds")
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
                    print((x + i), ", ", (y - i), "  not in bounds")
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
                    print((x + i), ", ", (y - i), "  not in bounds")
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
            
            


        print(positions)
        return positions

        
        



    def printBoard(self):
        for row in self.board:
            print(row)

