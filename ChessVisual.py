import tkinter as tk
from PIL import Image, ImageTk
import Pieces
from Chess import *

class ChessVisual:

    # Define constant size of chess board size

    def __init__(self, game : Chess) -> None:

        # Create and draw tiles for window for the board
        self.window = ChessVisual.drawBoard()

        # Set the game state to the controlling game state, of type Chess
        self.game = game

        # Stores images to prevent from being garbage collected
        self.images = set()

        # Store the starting point of a selected square
        self.oldPosition = (0,0)

        # Stores potential moves for clicked piece to highlight
        self.selectedPotentialMoves = []

        # Stores whether the selected piece is moving
        self.moving = False

        # Stores the highlighted cells
        self.highlights = []

        # Set all of the pieces on the board
        self.setAllPieces()
        


        self.window.bind("<Button-1>", self.click)


    def drawBoard() -> tk:
        """
        Returns a tiled window chess board
        """

        # Create the window
        window = tk.Tk(screenName="Chess",baseName="Chess")


        # Create grids
        for i in range(Chess.BOARD_SIZE):

            for j in range(Chess.BOARD_SIZE):

                # draws alternating colors
                color = "burlywood3"
                if (i + j) % 2 == 0:
                    color = "LemonChiffon2"
                
                # Add the grid square to the window
                newFrame = tk.Frame(master=window, width=100, height=100, bg=color)
                newFrame.grid(row=i, column=j)            

        return window
    

    def setAllPieces(self):
        """
        Sets all of the pieces according to the game state, self.game
        """
        # Loop through the board
        for y, row in enumerate(self.game.board):
            for x, tile in enumerate(row):

                # Only set the piece if it is not empty
                if tile != 0:
                    # Set the given tile to the correct piece
                    self.setPiece(tile, x, y)


    def setPiece(self, piece : int, x : int, y : int):
        """
        Set a given piece using Piece enum to the new x and y position on the grid.
        """

        # Determine the piece to set given the piece value
        imagePath = "./PieceImages/"

        if piece == 1:
            imagePath += "WhitePawn"
        elif piece == 2:
            imagePath += "WhiteKnight"
        elif piece == 3:
            imagePath += "WhiteBishop"
        elif piece == 4:
            imagePath += "WhiteRook"
        elif piece == 5:
            imagePath += "WhiteQueen"
        elif piece == 6:
            imagePath += "WhiteKing"
        elif piece == -1:
            imagePath += "BlackPawn"
        elif piece == -2:
            imagePath += "BlackKnight"
        elif piece == -3:
            imagePath += "BlackBishop"
        elif piece == -4:
            imagePath += "BlackRook"
        elif piece == -5:
            imagePath += "BlackQueen"
        elif piece == -6:
            imagePath += "BlackKing"
        
        imagePath += ".png"

        # Create the image
        pieceImageTk = ImageTk.PhotoImage(file=imagePath)


        # Determine background color for piece
        total = x + y
        backgroundColor = "yellow"
        if total % 2 == 0:
            backgroundColor = "LemonChiffon2"
        else:
            backgroundColor = "burlywood3"
        
        # Create the canvas to place the image
        canvas = tk.Canvas(master=self.window, width=75, height=75, bg=backgroundColor, highlightthickness=0)
        
        canvas.grid(row=y, column=x)

        # Prevent photo from being garbage collected
        self.images.add(pieceImageTk)

        # Create tag name to later get the image
        tagName = str(x) + ", " + str(y)

        # Add image to the canvas
        canvas.create_image((0,0), image=pieceImageTk, anchor='nw', tag=tagName)


    def movePiece(self, oldX : int, oldY : int, newX : int, newY : int, capture : bool, moveInfo : tuple):
        """
        Move the piece from one position to another
        """

        # En Passant or Promotion occured, special operations in order
        if moveInfo[1] or moveInfo[2]:
            
            # TODO Promotion occured

            # En passant occured
            if moveInfo[2]:
                
                # Remove pawn captured
                pawnToRemove = self.window.grid_slaves(row=oldY, column=newX)[0]
                pawnToRemove.grid_remove()

                # Place pawn capturing on grid
                pieceToMove = self.window.grid_slaves(row=oldY, column=oldX)[0]
                pieceToMove.grid(row=newY, column=newX)



        else:

            # Get piece on grid
            pieceToMove = self.window.grid_slaves(row=oldY, column=oldX)[0]
            
            # Remove piece to move
            pieceToMove.grid_remove()


            # Capture occured (not en passant), remove piece underneath
            if capture:
                underneathPiece = self.window.grid_slaves(row=newY, column=newX)[0]
                underneathPiece.grid_remove()

            # Set new background color of the canvas
            total = newX + newY
            backgroundColor = "yellow"
            if total % 2 == 0:
                backgroundColor = "LemonChiffon2"
            else:
                backgroundColor = "burlywood3"

            pieceToMove.configure(bg=backgroundColor)

            # Set the position of the new piece
            pieceToMove.grid(row=newY, column=newX)


        # TODO Remove
        self.game.printBoard()

    
    def highlightPotentialMoves(self):
        """
        Highlights squares a selected piece is able to move to. Called by self.click
        """

        # Create highlight objects for every potential move position
        for toHighlight in self.selectedPotentialMoves:

            # Create a canvas object
            canvas = tk.Canvas(master=self.window, width=100, height=100, bd=0, highlightthickness=0)
            canvas.create_rectangle(0,0,100,100,fill="green")

            # Add canvas object to list of highlights
            self.highlights.append(canvas)

            # Add canvas to grid
            canvas.grid(row=toHighlight[1], column=toHighlight[0])

    
    def removeHighlights(self):
        """
        Removes the highlighted squares on the board. Called by self.click
        """
        for highlight in self.highlights:

            highlight.grid_remove()


    def click(self, event):
        
        # Here retrieving the size of the parent
        # widget relative to master widget
        x = event.x_root - self.window.winfo_rootx()
        y = event.y_root - self.window.winfo_rooty()
    
        # Get relative position of grid
        z = self.window.grid_location(x, y)

        print(z)
        justMoved = False

        # Determine if clicked piece is in the potential moves for selected piece
        if self.moving:

            for move in self.selectedPotentialMoves:

                # Moving the selected piece
                if z[0] == move[0] and z[1] == move[1]:

                    justMoved = True
                    self.moving = False
        
                    # Piece moved, remove the highlights
                    self.removeHighlights()

                    # Move piece in game representation
                    moveInfo = self.game.movePiece(self.oldPosition[0], self.oldPosition[1], move)

                    # TODO Promotion
                    
                    # Check for en passant capture

                    # Move piece visually
                    self.movePiece(self.oldPosition[0], self.oldPosition[1], move[0], move[1], move[2], moveInfo)


        # No piece was moved, select new piece
        if not justMoved:

            # Don't select an empty tile
            if self.game.board[z[1]][z[0]] != 0:

                # Remove any uneccesary highlights
                self.removeHighlights()

                # Piece selected, set stage to moving
                self.moving = True

                # Update the potential moves based on selected piece
                self.selectedPotentialMoves = self.game.canMoveTo(z[0], z[1])
                # print("SELECTING")

                # Highlight the selected piece's potential moves
                self.highlightPotentialMoves()

                # Store position as old position
                self.oldPosition = (z[0], z[1])





        




def main():

    g = Chess()

    c = ChessVisual(g)

    c.window.mainloop()

if __name__ == "__main__":
    main()
