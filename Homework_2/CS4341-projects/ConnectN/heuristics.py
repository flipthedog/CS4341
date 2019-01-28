# heursistics.py
# Floris van Rossum

def calculate_total(brd, col, player):
    score = 0

    y = 0
    # print("Attempted col: " + str(col))
    while y < brd.h and brd.board[y][col] != 0:
        y = y + 1

    y = y - 1
    # Move is at col, y

    #score += neighbor_score(brd, col, y, player)
    score += center_score(brd, col, player)
    #score += line_length(brd, col, y, player)

    return score

# Check the board for forced moves in player's favor
#
# PARAM [board.Board] brd: the board state
# PARAM [int] player: The player whose turn it is
# PARAM [int] col: The column to check for forced move
# RETURN [boolean]: Whether this is a forced move or not
def forced_moves(brd, col, player):
    # TODO: Check the board for forced moves
    # Only forced moves that are advantageous to the player
    # Might check after the forced moves to see if that leads to a winning board

    for cell in brd.board:
        None

# Check the board to see if there are lines at the position
#   which would be one less than required to win
def is_less_line_at(x, y, dx, dy):
    None

# Find moves that must be made to block the other player from winning
#
# PARAM [board.Board] brd: the board state
# PARAM [int] col: The column in which the token is played
# PARAM [int] player: The player whose turn it is
# RETURN [boolean]: Whether this is a blocking move or not
def is_block(brd, col, player):
    # TODO: Implement a method to check what opponent needs to play to win
    #       then play that column
    new_board = brd.copy()

    if player == 1:
        other_player = 2
    else:
        other_player = 1

    new_board.add_token(col)


# Return the maximum line length from a move
#
# PARAM [board.Board] brd: the board state
# PARAM [int] col: The column in which the token is played
# PARAM [int] player: The player whose turn it is
# RETURN [int]: Line length
def line_length(brd, col, y, player):

    if brd.get_outcome == player:
        return 100
    elif brd.get_outcome == brd.player:
        return - 100
    else:
        return 0

# Return the number of open spaces around the last move
#
# PARAM [board.Board] brd: the board state
# PARAM [int] col: The column in which the token is played
# PARAM [int] player: The player whose turn it is
# RETURN [int]: Number of open spaces
def neighbor_score(brd, col, y, player):
    # TODO: Implement a method to find open spaces surrounding move
    score = 0

    score += calculate_surrounding_score(brd, player, col, y)

    return score


def calculate_surrounding_score(brd, player, x, y):
    score = 0

    # print("Home cell: " + str(brd.board[y][x]))
    # print("Player cell: " + str(player))

    # Check below
    if (y - 1 > 0):
        cell = brd.board[y - 1][x]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check left
    if (x - 1 > 0):
        cell = brd.board[y][x - 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check right
    if (x + 1 < brd.w):
        # print("y, x: " + str(y) + ", " + str(x))
        cell = brd.board[y][x + 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check top left
    if (x - 1 > 0) and (y + 1 < brd.h):
        cell = brd.board[y + 1][x - 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check top right
    if (x + 1 < brd.w) and (y + 1 < brd.h):
        cell = brd.board[y + 1][x + 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check bottom left
    if (x - 1 > 0) and (y - 1 > 0):
        cell = brd.board[y - 1][x - 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    # Check bottom right
    if (x + 1 < brd.w) and (y - 1 > 0):
        cell = brd.board[y - 1][x + 1]

        if cell == 0:
            score += 3
        elif cell == player:
            score += 5

    return score
# Return the number of open spaces around the last move
#
# PARAM [board.Board] brd: the board state
# PARAM [int] col: The column in which the token is played
# PARAM [int] player: The player whose turn it is
# RETURN [int]: Score achieved through center control
def center_score(brd, col, player):
    # TODO Determine a scoring system based on center
    #      board control
    # Columns at (width / 2) increase score by 3
    # Rows at (height / 2) increase score by 3

    score = 0

    for i in range(brd.w):

        num = 0
        opp_num = 0

        for j in range(brd.h):

            if brd.board[j][i] == player:
                num += 1
            else:
                opp_num += 1

        distance_from_center = abs(int(brd.w / 2) - i)

        if distance_from_center == 0:
            score += num * 10 - opp_num * 10
        elif distance_from_center == 1:
            score += num * 5 - opp_num * 5
        elif distance_from_center == 2:
            score += num * 3 - opp_num * 3
        elif distance_from_center == 3:
            score += num * 2 - opp_num * 3
        elif distance_from_center == 4:
            score += num * 1 - opp_num * 1

    # new_board = brd.copy()
    #
    # width = new_board.w
    #
    # distance_from_center = abs(int(width/2) - col)
    #
    # if distance_from_center == 0:
    #     score = 10
    # elif distance_from_center == 1:
    #     score = 5
    # elif distance_from_center == 2:
    #     score = 3
    # elif distance_from_center == 3:
    #     score = 2
    # elif distance_from_center == 4:
    #     score = 1

    return score
