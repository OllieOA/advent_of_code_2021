import argparse
import time

import numpy as np


def fold_x_times(paper, folds, n):
    i = 0
    while i < n:
        try:
            fold = folds[i]
        except IndexError:
            print("Max folds achieved")
            return paper
        if fold[0] == "x":
            fold_base = paper[:, 0 : fold[1]]
            fold_added = paper[:, fold[1] + 1 :]
            paper = fold_base + np.fliplr(fold_added)
        elif fold[0] == "y":
            fold_base = paper[0 : fold[1], :]
            fold_added = paper[fold[1] + 1 :, :]
            paper = fold_base + np.flipud(fold_added)
        i += 1

    return paper


def main(args):
    print("=" * 40, " FILE I/O  ", "=" * 40)
    start_time0 = time.time()
    if args.test:
        input_path = "day13/day13_test.txt"
    else:
        input_path = "day13/day13_input.txt"

    with open(input_path, "r") as f:
        lines = f.readlines()

    folds = []
    coords = []
    for line in lines:
        if line[0].isnumeric():
            coords.append(tuple([int(x) for x in line.strip("\n").split(",")]))
        elif line.startswith("fold"):
            folds.append((line.split("=")[0][-1], int(line.strip("\n").split("=")[1])))

    coords = np.array(coords)
    stop_time0 = time.time()
    print(f"File IO finished in {(stop_time0 - start_time0) * 1000} milliseconds")

    print("=" * 40, " PART ONE ", "=" * 40)  #### PART 1 ####
    start_time1 = time.time()

    # Figure out paper size
    x_max = np.max(coords[:, 0])
    y_max = np.max(coords[:, 1])

    paper = np.zeros((y_max + 1, x_max + 1))
    for coord in coords:
        paper[coord[1], coord[0]] = 1

    final_paper = fold_x_times(paper, folds, 1)
    answer = np.count_nonzero(final_paper)

    stop_time1 = time.time()
    print(
        f"Final answer: {answer}, found in {(stop_time1 - start_time1) * 1000} milliseconds"
    )

    print("=" * 40, " PART TWO ", "=" * 40)  #### PART 2 ####
    start_time2 = time.time()

    final_paper = fold_x_times(paper, folds, len(folds))
    final_paper_str = np.zeros(final_paper.shape, str)

    for idx, val in np.ndenumerate(final_paper):
        if val > 0:
            final_paper_str[idx] = "#"
        else:
            final_paper_str[idx] = "."

    for row in final_paper_str:
        print("".join(row))

    stop_time2 = time.time()

    print(
        f"Final answer: (printed), found in {(stop_time2 - start_time2) * 1000} milliseconds"
    )

    print("=" * 40, "   END    ", "=" * 40)  #### PART 1 ####


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--test", action="store_true")

    args = arg.parse_args()

    main(args)
