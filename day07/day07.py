def calc_fuel_constant(initial_pos, desired_spot):
    pos_count = dict()
    for i in initial_pos:
        pos_count[i] = pos_count.get(i, 0) + 1

    fuel_spent = 0
    for key, val in pos_count.items():
        fuel_spent += abs(key - desired_spot) * val

    return fuel_spent


def calc_fuel_linear(initial_pos, desired_spot):
    pos_count = dict()
    for i in initial_pos:
        pos_count[i] = pos_count.get(i, 0) + 1

    fuel_spent = 0
    for key, val in pos_count.items():
        dist = abs(key - desired_spot)
        linear_cost = (dist * (dist + 1)) // 2
        fuel_spent += linear_cost * val

    return fuel_spent


print("=" * 40, " PART ONE ", "=" * 40)

with open("day07\day07_input.txt", "r") as f:
    initial_pos = [int(x) for x in f.read().split(",")]

average_pos = int(sum(initial_pos) / len(initial_pos))
spread = (max(initial_pos) - min(initial_pos)) // 8
check_vals = range(average_pos - spread, average_pos + spread)

curr_fuel_cost = 1e9
curr_best_pos = 0

for val in check_vals:
    staged_best_fuel_cost = curr_fuel_cost
    curr_fuel_cost = min(curr_fuel_cost, calc_fuel_constant(initial_pos, val))

    if curr_fuel_cost < staged_best_fuel_cost:
        curr_best_pos = val

print("best pos: {}\nwith fuel cost: {}".format(curr_best_pos, curr_fuel_cost))


print("=" * 40, " PART TWO ", "=" * 40)

curr_fuel_cost = 1e9
curr_best_pos = 0

for val in check_vals:
    staged_best_fuel_cost = curr_fuel_cost
    curr_fuel_cost = min(curr_fuel_cost, calc_fuel_linear(initial_pos, val))

    if curr_fuel_cost < staged_best_fuel_cost:
        curr_best_pos = val
print("best pos: {}\nwith fuel cost: {}".format(curr_best_pos, curr_fuel_cost))

print("=" * 40, "    END   ", "=" * 40)
