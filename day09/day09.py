import math
import numpy as np
import timeit


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


def get_adjacent_cart(pos, map_shape):
    cart_pos = [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    ]

    adjacent_pos = remove_invalid(cart_pos, map_shape)
    return adjacent_pos


print("=" * 40, " PART ONE ", "=" * 40)

heightmap = []

with open("day09\day09_input.txt", "r") as f:
    lines = f.readlines()

start_time = timeit.default_timer()
for line in lines:
    heightmap.append([int(x) for x in line.strip("\n")])

heightmap = np.array(heightmap)
low_points = []

for pos, val in np.ndenumerate(heightmap):
    adjacent_pos = get_adjacent_cart(pos, heightmap.shape)

    if all(heightmap[a_pos[0], a_pos[1]] > val for a_pos in adjacent_pos):
        low_points.append((pos, val))

total_score = 0
for point in low_points:
    total_score += 1 + point[1]

stop_time = timeit.default_timer()
print("execution time: {} seconds".format(stop_time - start_time))

print(f"final result: {total_score}")

print("=" * 40, " PART TWO ", "=" * 40)

goal_set = set([goal_pos[0] for goal_pos in low_points])
basins = {low_point[0]: [] for low_point in low_points}

for pos, val in np.ndenumerate(heightmap):
    if val == 9:
        continue

    visited = set([])
    queue = [pos]

    while queue:
        curr_node = queue.pop(0)
        visited.add(curr_node)

        if curr_node in goal_set:
            # Assign point to basin
            basins[curr_node].append(pos)
            break

        else:
            neighbours = get_adjacent_cart(curr_node, heightmap.shape)
            new_neighbours = [
                neighbour
                for neighbour in neighbours
                if (neighbour not in visited)
                and (heightmap[neighbour] < heightmap[curr_node])
                and (heightmap[neighbour] != 9)
            ]

            queue += new_neighbours

# Visualise

# for point, basin in basins.items():
#     demo_array = np.ones(heightmap.shape).astype(str)
#     demo_array[demo_array == "1.0"] = "."
#     for basin_point in basin:
#         demo_array[basin_point[0], basin_point[1]] = str(
#             heightmap[basin_point[0], basin_point[1]]
#         )
#     print("\n\n")
#     print(demo_array)
#     print("\n\n")

basin_sizes = sorted([len(basin) for basin in basins.values()], reverse=True)
print("final value: ", math.prod(basin_sizes[:3]))

print("=" * 40, "   END    ", "=" * 40)
