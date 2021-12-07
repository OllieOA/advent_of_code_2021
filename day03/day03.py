import numpy as np


def part_two(input_array, mode):
    for col in range(input_array.shape[1]):
        col_array = input_array[:, col]

        count_0 = np.count_nonzero(col_array == "0")
        count_1 = np.count_nonzero(col_array == "1")

        # Reduce curr_array

        new_array = np.empty((0, input_array.shape[1]), str)

        if count_0 > count_1:
            common_bit = str(mode)  # 0
        elif count_0 < count_1:
            common_bit = str(abs(mode - 1))  # 1
        else:
            common_bit = str(abs(mode - 1))  # 1

        for row in range(input_array.shape[0]):
            if input_array[row, col] == common_bit:
                new_array = np.append(new_array, [input_array[row, :]], axis=0)

        input_array = new_array.copy()
        if input_array.shape[0] == 1:
            return input_array

    return None


bin_array = None
# bin_array = np.empty((0, 12), str)
# bin_array = np.empty((0, 5), str)
with open("day03\day03_input.txt", "r") as f:
    # with open("day03\day03_test.txt", "r") as f:
    for line in f.readlines():
        if bin_array is None:
            bin_array = np.empty((0, len(line.strip("\n"))), str)
        bin_row = [char for char in line if (char == "1" or char == "0")]
        bin_row_np = np.array([bin_row])
        bin_array = np.append(bin_array, bin_row_np, axis=0)

gamma = ""
epsilon = ""

for col in range(bin_array.shape[1]):
    col_array = bin_array[:, col]

    count_0 = np.count_nonzero(col_array == "0")
    count_1 = np.count_nonzero(col_array == "1")

    if count_0 > count_1:
        gamma += "0"
        epsilon += "1"
    elif count_0 < count_1:
        gamma += "1"
        epsilon += "0"
    else:
        print("Equal amount!")

print("gamma: ", gamma)
print("epsilon: ", epsilon)

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print("gamma_dec: ", gamma_dec)
print("epsilon_dec: ", epsilon_dec)
print("Final answer: ", gamma_dec * epsilon_dec)

print("=" * 80)

# Part 2
oxy_array = bin_array.copy()
co2_array = bin_array.copy()

oxy_array = part_two(oxy_array, 0)
co2_array = part_two(co2_array, 1)

oxy_dec = int("".join(oxy_array[0, :]), 2)
co2_dec = int("".join(co2_array[0, :]), 2)

print("oxy: ", oxy_dec)
print("co2: ", co2_dec)
print("Final answer: ", oxy_dec * co2_dec)
