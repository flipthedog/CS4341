import math
import agent

###########################
# Alpha-Beta Search Agent #
###########################

class AlphaBetaAgent(agent.Agent):
    """Agent that uses alpha-beta search"""

    # Class constructor.
    #
    # PARAM [string] name:      the name of this player
    # PARAM [int]    max_depth: the maximum search depth
    def __init__(self, name, max_depth):
        super().__init__(name)
        # Max search depth
        self.max_depth = max_depth
        self.cutoff = False
        self.neg_inf = - 999999999
        self.pos_inf = 9999999999

    # Pick a column.
    #
    # PARAM [board.Board] brd: the current board state
    # RETURN [int]: the column where the token must be added
    #
    # NOTE: make sure the column is legal, or you'll lose the game.
    def go(self, brd):
        """Search for the best move (choice of column for the token)"""
        # Your code here

    # Get the successors of the given board.
    #
    # PARAM [board.Board] brd: the board state
    # RETURN [list of (board.Board, int)]: a list of the successor boards,
    #                                      along with the column where the last
    #                                      token was added in it
    def get_successors(self, brd):
        """Returns the reachable boards from the given board brd. The return value is a tuple (new board state, column number where last token was added)."""
        # Get possible actions
        freecols = brd.free_cols()
        # Are there legal actions left?
        if not freecols:
            return []
        # Make a list of the new boards along with the corresponding actions
        succ = []
        for col in freecols:
            # Clone the original board
            nb = brd.copy()
            # Add a token to the new board
            # (This internally changes nb.player, check the method definition!)
            nb.add_token(col)
            # Add board to list of successors
            succ.append((nb,col))
        return succ

    # Return an action
    def alpha_beta_search(self, brd, depth):
        column = 2

        v = self.max_value(brd, self.neg_inf, self.pos_inf)

        return column

    # Return max value
    def max_value(self, brd, alpha, beta, depth):

        if self.cutoff_test(brd, depth):
            return self.evaluation()

        v = self.neg_inf

        for (a, s) in self.get_successors(brd):

            v = max(v, self.min_value(s, alpha, beta, depth + 1))

            if v >= beta:

                return v

            alpha = max(alpha, v)

        return v

    # Return min value
    def min_value(self, brd, alpha, beta, depth):

        if self.cutoff_test(brd, depth):
            return self.evaluation()

        v = self.pos_inf

        for (a, s) in self.get_successors(brd):
            v = min(v, self.max_value(brd, alpha, beta, depth + 1))

            if v <= alpha:

                return v

            beta = min(beta, v)

        return v

    # Put in some logic here to determine if cutoff is reached
    def cutoff_test(self, brd, depth):
        None

    # Determine the value of the board state
    def evaluation(self):
        None

    # Resources Used:
    # 1. http://aima.cs.berkeley.edu/python/games.html