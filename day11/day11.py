import numpy as np
import time


def remove_invalid(pos_list, map_shape):
    valid_pos = []
    for sub_pos in pos_list:
        if not (
            (sub_pos[0] < 0 or sub_pos[0] >= map_shape[0])
            or (sub_pos[1] < 0 or sub_pos[1] >= map_shape[1])
        ):
            # If position is not out of bounds, add it
            valid_pos.append(sub_pos)

    return valid_pos


def get_adjacent_eight(pos, map_shape):
    cart_pos = [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1] + 1),
        (pos[0] - 1, pos[1] - 1),
        (pos[0] - 1, pos[1] + 1),
        (pos[0] + 1, pos[1] - 1),
    ]

    adjacent_pos = remove_invalid(cart_pos, map_shape)
    return adjacent_pos


def run_for_step(octos):
    flash_count_for_step = 0
    expended = []
    init = True
    start_time = time.time()
    while np.any((octos > 9)) or init:
        if init:
            octos += 1
            init = False

        highlights = []
        for pos, val in np.ndenumerate(octos):
            if val > 9 and pos not in expended:
                highlights.append(pos)

        for flash in highlights:
            flash_count_for_step += 1
            expended.append(flash)
            octos[flash] = 0

            neighbours = get_adjacent_eight(flash, octos.shape)
            for neighbour in neighbours:
                if neighbour not in expended:
                    octos[neighbour] += 1

    if flash_count_for_step > 0:
        stop_time = time.time()
        exec_time = 1000000 * (stop_time - start_time)
    else:
        exec_time = -1

    return octos, flash_count_for_step, exec_time


print("=" * 40, " PART ONE ", "=" * 40)

octos = []

with open("day11/day11_input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    octos.append([int(x) for x in line.strip("\n")])

octos = np.array(octos)
octos_p2 = octos.copy()

flash_count = 0
loop_times = []
for n in range(100):
    octos, flash_count_for_step, exec_time = run_for_step(octos)
    flash_count += flash_count_for_step
    if exec_time > 0:
        loop_times.append(exec_time)

print(f"Final answer: {flash_count}")

print(
    f"Time stats:\nAverage: {np.mean(loop_times)}\nStd: {np.std(loop_times)}\nPercentiles: \nFirst: {np.percentile(loop_times, 25)}\nSecond: {np.percentile(loop_times, 50)}\nThird: {np.percentile(loop_times, 75)}"
)

print("=" * 40, " PART TWO ", "=" * 40)

n = 0
while not np.all((octos_p2 == 0)):
    n += 1
    octos_p2, flash_count_for_step, exec_time = run_for_step(octos_p2)

print(f"Final answer: {n}")
