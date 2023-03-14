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
        canvas = tk.Canvas(master=self.window, width=75, height=75, bg=backgroundColor)
        
        canvas.grid(row=y, column=x)

        # Prevent photo from being garbage collected
        self.images.add(pieceImageTk)

        # Add image to the canvas
        canvas.create_image((0,0), image=pieceImageTk, anchor='nw')
    
    def movePiece(self, oldX : int, oldY : int, newX : int, newY : int):
        """
        Move the piece from one position to another
        """

        # Get piece on grid
        pieceToMove = self.window.grid_slaves(row=oldY, column=oldX)[0]
        piece = pieceToMove.cget("text")
        
        # Remove piece to move
        pieceToMove.grid_remove()

        # Create the piece at the new position
        label = tk.Label(self.window, text=piece)
        label.grid(row=newY, column=newX)

    
    
    def click(self, event):
        
        # Here retrieving the size of the parent
        # widget relative to master widget
        x = event.x_root - self.window.winfo_rootx()
        y = event.y_root - self.window.winfo_rooty()
    
        # Here grid_location() method is used to
        # retrieve the relative position on the
        # parent widget
        z = self.window.grid_location(x, y)
    
        # printing position
        print(z)




def main():

    g = Chess()

    c = ChessVisual(g)

    c.window.mainloop()

if __name__ == "__main__":
    main()
