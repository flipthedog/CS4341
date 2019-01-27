# Floris van Rossum
# CS4341 - Homework 1
# Professor Carlo Pinciroli
# Exercise 1
# ex1.py

class ConnectFour:
    """Connect four game"""

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""

        # The player (1 or 2) we are testing the line for to see if they won
        player = self.board[y][x]

        # Test for directional line
        if dx == 0 and dy == 1:
            # Vertical line

            # Move out 3 more spaces
            for i in range(1, 4):

                # Check if the square is the same as the player square
                if (y + i) < self.h:
                    cell = self.board[y + i][x]

                    if not cell == player:
                        # Cell is not same as player, not a line
                        return False
                else:
                    # End of board reached, not a line
                    return False

            # print("Won because vertical line")
            # Line at this point
            return True

        elif dx == 1 and dy == 0:
            # Horizontal line

            for i in range(1, 4):

                if (x + i) < self.w - 1:
                    cell = self.board[y][x + i]

                    if not cell == player:
                        return False
                else:
                    return False

            # print("Won because horizontal line")
            return True

        elif dx == 1 and dy == 1:
            # Diagonal down
            for i in range(1, 4):

                if ((x + i) < self.w - 1) and ((y + i) < self.h - 1):

                    cell = self.board[y + i][x + i]

                    if not cell == player:
                        return False
                else:
                    return False

            # print("Won because down diagonal")
            return True

        elif dx == 1 and dy == -1:
            # Diagonal up
            for i in range(1, 3):

                if ((x + i) < self.w - 1) and ((y - i) > 0):
                    cell = self.board[y - i][x + i]

                    if not cell == player:
                        return False
                else:
                    return False

            # print("Won because up diagonal")
            return True

    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        # Debugging Statement: # print("Checking: " + str(self.board[y][x]) + " at " + "(" + str(x) + " ," + str(y) + ")")
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        # Your code here, use isAnyLineAt()

        # Loop through all spaces
        for width in range(0, self.w):

            for height in range(0, self.h):

                # If the space is not 0, test for line
                if not self.board[height][width] == 0:

                    # See if there is a line
                    if self.isAnyLineAt(width, height):

                        # Check who won
                        if self.board[height][width] == 1:
                            # Cell contains a 1, player 1 won
                            return 1

                        if self.board[height][width] == 2:
                            # Cell contains a 2, player 2 won
                            return 2

        return 0

    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome() # Find the outcome of the game
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")
