import argparse
import time


def main(args):
    print("=" * 40, " FILE I/O  ", "=" * 40)
    start_time0 = time.time()

    if args.test:
        input_path = "day14/day14_test.txt"
    else:
        input_path = "day14/day14_input.txt"

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        pass

    stop_time0 = time.time()
    print(f"File IO finished in {(stop_time0 - start_time0) * 1000} milliseconds")

    print("=" * 40, " PART ONE ", "=" * 40)  #### PART 1 ####
    start_time1 = time.time()
    answer = "PLACEHOLDER"
    stop_time1 = time.time()
    print(
        f"Final answer: {answer}, found in {(stop_time1 - start_time1) * 1000} milliseconds"
    )

    print("=" * 40, " PART TWO ", "=" * 40)  #### PART 2 ####
    start_time2 = time.time()
    answer = "PLACEHOLDER"
    stop_time2 = time.time()
    print(
        f"Final answer: {answer}, found in {(stop_time2 - start_time2) * 1000} milliseconds"
    )


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--test", action="store_true")

    args = arg.parse_args()

    main(args)
