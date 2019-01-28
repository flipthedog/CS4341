import math
import agent
import board
import heuristics

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
        self.neg_inf = - 9999999999999
        self.pos_inf = 999999999999
        self.best_move_col = -1

    # Pick a column.
    #
    # PARAM [board.Board] brd: the current board state
    # RETURN [int]: the column where the token must be added
    #
    # NOTE: make sure the column is legal, or you'll lose the game.
    def go(self, brd):
        """Search for the best move (choice of column for the token)"""
        # Your code here
        return self.alpha_beta_search(brd)

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
    def alpha_beta_search(self, brd):

        best_value = self.neg_inf

        for (state, col) in self.get_successors(brd):

            returnArr = self.max_value(state, col, self.neg_inf, self.pos_inf, 0)

            v = returnArr[0]
            best_move = returnArr[1]

            if v > best_value:
                best_value = v
                #print("Best Score: " + str(best_value))
                self.best_move_col = best_move

        return self.best_move_col

    # Return max value
    def max_value(self, brd, action, alpha, beta, depth):

        if self.cutoff_test(brd, depth):

            return [self.evaluation(brd, action), action]

        bestVal = self.neg_inf
        bestMove = None
        for (state, col) in self.get_successors(brd):

            returnArr = self.min_value(state, col, alpha, beta, depth + 1)
            v = returnArr[0]
            move = returnArr[1]

            if v > bestVal:
                bestMove = move
                bestVal = v

            if bestVal >= beta:

                return [bestVal, bestMove]

            alpha = max(alpha, bestVal)

        return [bestVal, bestMove]

    # Return min value
    def min_value(self, brd, action, alpha, beta, depth):

        if self.cutoff_test(brd, depth):

            return [self.evaluation(brd, action), action]

        min_val = self.pos_inf
        bestMove = None

        for (state, col) in self.get_successors(brd):

            returnArr = self.max_value(state, col, alpha, beta, depth + 1)
            v = returnArr[0]
            move = returnArr[1]

            if v < min_val:
                min_val = v
                bestMove = move

            if min_val <= alpha:

                return [min_val, bestMove]

            beta = min(beta, min_val)

        return [min_val, bestMove]

    # Put in some logic here to determine if cutoff is reached
    def cutoff_test(self, brd, depth):
        if depth > self.max_depth:
            return True

        if brd.get_outcome() is not 0:
            # Terminal state, player won
            return True

        return False
        # TODO: Put logic here to determine terminal state

    # Determine the value of the board state
    def evaluation(self, brd, col):
        # TODO: Call heuristics function

        if brd.player == 1:
            player = 2
        else:
            player = 1

        score = heuristics.calculate_total(brd, col, player)

        # print("\n\nBOARD TEST: " + str(col) + " last move!")
        # brd.print_it()
        # print("THIS WAS THE SCORE: " + str(score))
        # input()

        return score

    # Resources Used:
    # 1. http://aima.cs.berkeley.edu/python/games.html
    # 2. https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/