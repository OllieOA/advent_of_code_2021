import argparse
import time

from numpy import inf


def get_max_vs_min(counts):
    min_val = inf
    max_val = 0

    for key in counts.keys():
        if counts[key] > max_val:
            max_key = key
            max_val = counts[key]
        if counts[key] < min_val:
            min_key = key
            min_val = counts[key]

    return counts[max_key] - counts[min_key]


def get_polymer_counts(initial_polymer, pair_insertions, turns):
    polymer = initial_polymer
    for _ in range(turns):
        new_polymer = polymer[0]
        for pair_num in range(len(polymer) - 1):
            pair = polymer[pair_num] + polymer[pair_num + 1]
            new_polymer += pair_insertions[pair] + pair[1]
        polymer = new_polymer

    counts = dict((x, polymer.count(x)) for x in set(polymer))
    return counts


def get_polymer_counts_efficient(initial_polymer, pair_insertions, turns):
    polymer = initial_polymer
    pair_dict = {}
    for pair_num in range(len(polymer) - 1):
        pair_key = polymer[pair_num] + polymer[pair_num + 1]
        try:
            pair_dict[pair_key] += 1
        except KeyError:
            pair_dict.update({pair_key: 1})

    for _ in range(turns):
        new_pairs_dict = {}
        for pair_key, pair_val in pair_dict.items():
            new_pairs = [
                pair_key[0] + pair_insertions[pair_key],
                pair_insertions[pair_key] + pair_key[1],
            ]

            for new_pair in new_pairs:
                try:
                    new_pairs_dict[new_pair] += pair_val
                except KeyError:
                    new_pairs_dict.update({new_pair: pair_val})

        pair_dict = new_pairs_dict.copy()

    counts = {}
    for key, val in pair_dict.items():
        try:
            counts[key[1]] += val
        except KeyError:
            counts.update({key[1]: val})

    return counts


def main(args):
    print("=" * 40, " FILE I/O  ", "=" * 40)
    start_time0 = time.time()

    if args.test:
        input_path = "day14/day14_test.txt"
    else:
        input_path = "day14/day14_input.txt"

    with open(input_path, "r") as f:
        lines = f.readlines()

    first_line = True
    pair_insertions = {}
    for line in lines:
        if first_line:
            first_line = False
            polymer = line.strip("\n")
        else:
            if line.strip("\n"):
                line_split = line.strip("\n").split(" -> ")
                pair_insertions.update({line_split[0]: line_split[1]})

    stop_time0 = time.time()
    print(f"File IO finished in {(stop_time0 - start_time0) * 1000} milliseconds")

    print("=" * 40, " PART ONE ", "=" * 40)  #### PART 1 ####
    start_time1 = time.time()

    counts = get_polymer_counts(polymer, pair_insertions, 10)

    answer = get_max_vs_min(counts)

    stop_time1 = time.time()
    print(
        f"Final answer: {answer}, found in {(stop_time1 - start_time1) * 1000} milliseconds"
    )

    print("=" * 40, " PART TWO ", "=" * 40)  #### PART 2 ####
    start_time2 = time.time()

    counts = get_polymer_counts_efficient(polymer, pair_insertions, 40)
    answer = get_max_vs_min(counts)

    stop_time2 = time.time()
    print(
        f"Final answer: {answer}, found in {(stop_time2 - start_time2) * 1000} milliseconds"
    )


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--test", action="store_true")

    args = arg.parse_args()

    main(args)

    # NOT 3562403467316
