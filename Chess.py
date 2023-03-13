import tkinter as tk
from enum import Enum
import Pieces

class Chess:


    def __init__(self) -> None:

        # Create and draw tiles for window for the board
        self.window = Chess.drawBoard()

        self.setPiece(1, 1, 1)
        self.movePiece(1,1,2,3)

        self.window.bind("<Button-1>", self.click)


    def drawBoard() -> tk:
        """
        Returns a tiled window chess board
        """

        # Create the window
        window = tk.Tk(screenName="Chess",baseName="Chess")

        # board size is 8 x 8
        boardSize = 8

        # Create grids
        for i in range(boardSize):

            for j in range(boardSize):

                # draws alternating colors
                color = "black"
                if (i + j) % 2 == 0:
                    color = "white"
                
                # Add the grid square to the window
                newFrame = tk.Frame(master=window, width=100, height=100, bg=color)
                newFrame.grid(row=i, column=j)            

        return window
    




    def setPiece(self, piece : int, newX : int, newY : int):
        """
        Set a given piece using Piece enum to the new x and y position on the grid.
        """
        label = tk.Label(self.window, text=piece)
        label.grid(row=newY, column=newX)

    
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

    c = Chess()

    c.window.mainloop()

if __name__ == "__main__":
    main()
