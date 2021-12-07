import numpy as np


def cart_line_generator(input_list):
    x1, y1, x2, y2 = input_list
    output_coords = []
    if x1 != x2:
        # Horizontal line
        max_x = max(x1, x2)
        min_x = min(x1, x2)
        x_pos_list = list(range(min_x, max_x + 1))
        for x_pos in x_pos_list:
            output_coords.append([x_pos, y1])
    else:
        # Vert line
        max_y = max(y1, y2)
        min_y = min(y1, y2)
        y_pos_list = list(range(min_y, max_y + 1))
        for y_pos in y_pos_list:
            output_coords.append([x1, y_pos])
    return output_coords


def line_generator(input_list):
    x1, y1, x2, y2 = input_list
    output_coords = []

    if x2 > x1:
        x_dir = 1
    else:
        x_dir = -1

    if y2 > y1:
        y_dir = 1
    else:
        y_dir = -1

    max_x = max(x1, x2)
    min_x = min(x1, x2)
    max_y = max(y1, y2)
    min_y = min(y1, y2)

    line_len = max(max_x - min_x, max_y - min_y)

    vert = max_x == min_x
    horiz = max_y == min_y

    x_pos_list = list(range(x1, x2 + x_dir, x_dir))
    y_pos_list = list(range(y1, y2 + y_dir, y_dir))

    if horiz and not vert:
        y_pos_list = [max_y] * (line_len + 1)
    elif vert and not horiz:
        x_pos_list = [max_x] * (line_len + 1)

    assert len(x_pos_list) == len(y_pos_list), "Must be same length!"

    for x_pos, y_pos in zip(x_pos_list, y_pos_list):
        output_coords.append([x_pos, y_pos])

    return output_coords


print("=" * 40, " PART ONE ", "=" * 40)

coords = []

max_x = 0
max_y = 0

with open("day05\day05_input.txt", "r") as f:
    for line in f.readlines():
        stripped_line = line.strip("\n").replace(" -> ", ",")
        stripped_coords = [int(x) for x in stripped_line.split(",")]
        coords.append(stripped_coords)

        max_x = max(max_x, stripped_coords[0])
        max_x = max(max_x, stripped_coords[2])
        max_y = max(max_y, stripped_coords[1])
        max_y = max(max_y, stripped_coords[3])

board = np.zeros((max_x + 1, max_y + 1))

for coord in coords:
    if coord[0] == coord[2] or coord[1] == coord[3]:
        # Valid straight line
        line_coords = cart_line_generator(coord)
        for line_coord in line_coords:
            board[line_coord[0], line_coord[1]] += 1

board_to_count = np.where(board <= 1, 0, board)
count = np.count_nonzero(board_to_count)
print("Final answer: ", count)

print("=" * 40, " PART TWO ", "=" * 40)

board_full = np.zeros((max_x + 1, max_y + 1))

for coord in coords:
    line_coords = line_generator(coord)
    for line_coord in line_coords:
        board_full[line_coord[0], line_coord[1]] += 1

board_to_count = np.where(board_full <= 1, 0, board_full)
count = np.count_nonzero(board_to_count)
print("Final answer: ", count)

print("=" * 40, "    END   ", "=" * 40)
