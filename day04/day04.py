import numpy as np


def win_check(board):
    """
    >>> print(win_check(np.array([["X", "X", "X"], [1, 2, 3], [4, 5, 6]])))
    True
    >>> print(win_check(np.array([[1, "X", 2], [3, "X", "X"], [4, "X", 5]])))
    True
    >>> print(win_check(np.array([[1, 2], [3, "X"]])))
    False
    """

    for row in board:
        if set(row) == set({"X"}):
            return True

    for col in board.T:
        if set(col) == set({"X"}):
            return True

    return False


print("PART ONE")

bingo_boards = []
with open("day04/day04_input.txt", "r") as f:
    first_line = True
    raw_boards = []
    for line in f.readlines():
        if first_line:
            bingo_game = line
            first_line = False
        else:
            raw_boards.append(line)

bingo_game = [x for x in bingo_game.strip("\n").split(",")]

for board_i in range(len(raw_boards)):
    curr_board = np.empty((0, 5), str)
    if raw_boards[board_i] == "\n":
        complete_raw_board = raw_boards[board_i + 1 : board_i + 6]
        for board_line in complete_raw_board:
            spaced_line = " ".join(board_line.strip("\n").split())
            stripped_line = [str(int(x)) for x in spaced_line.split(" ")]
            curr_board = np.append(curr_board, np.array([stripped_line]), axis=0)

        bingo_boards.append(curr_board)

bingo_boards = np.array(bingo_boards)
bingo_boards_part_2 = bingo_boards.copy()


won = False
for turn in bingo_game:
    new_boards = []
    for board in bingo_boards:
        curr_board = np.where(board == turn, "X", board)

        if win_check(curr_board):
            winning_board = curr_board
            winning_turn = turn
            won = True
            break

        new_boards.append(curr_board)
    if won:
        break
    bingo_boards = np.array(new_boards)

# Calculate the win
winning_board = np.where(winning_board == "X", "0", winning_board)
winning_board = winning_board.astype(int)

non_zero_sum = np.sum(winning_board)
print("Final result: {}".format(non_zero_sum * int(winning_turn)))


print("=" * 80)
print("PART TWO")

lost = False
won = False
for turn in bingo_game:
    new_boards = []
    for board in bingo_boards_part_2:
        curr_board = np.where(board == turn, "X", board)

        if lost:
            # Check for game win
            if win_check(curr_board):
                won = True
                losing_board = curr_board
                losing_turn = turn

        if not win_check(curr_board):
            # Do not include board
            new_boards.append(curr_board)

    if len(new_boards) == 1 and not lost:
        # Game will be lost successfully
        lost = True
    bingo_boards_part_2 = np.array(new_boards)
    if won and lost:
        break

losing_board = np.where(losing_board == "X", "0", losing_board)
losing_board = losing_board.astype(int)
non_zero_sum = np.sum(losing_board)
print("losing board sum: ", non_zero_sum)
print("losing turn: ", losing_turn)
print("Final result: {}".format(non_zero_sum * int(losing_turn)))

print("=" * 40, " END ", "=" * 40)
