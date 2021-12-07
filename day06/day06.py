import timeit


def get_fish_population(days, initial_age):

    fish_age = initial_age.copy()

    for day in range(days):

        next_fish_age = []
        new_fish = []
        for age in fish_age:
            append_age = age - 1
            if append_age == -1:
                new_fish.append(8)
                append_age = 6

            next_fish_age.append(append_age)
        next_fish_age.extend(new_fish)

        fish_age = next_fish_age.copy()

        age_count = dict()
        for i in fish_age:
            age_count[i] = age_count.get(i, 0) + 1

    print("total of {} fish after {} days".format(len(fish_age), day + 1))

    return None


def get_fish_population_efficient(days, initial_age):
    age_count = dict()
    for i in initial_age:
        age_count[i] = age_count.get(i, 0) + 1

    for day in range(days):
        new_count = dict()
        for key, val in age_count.items():
            new_count[key - 1] = val  # Increase fish age

        # Find fish to birth
        if -1 in new_count.keys():
            new_count[8] = new_count[-1]
            try:
                new_count[6] += new_count[-1]
            except:
                new_count[6] = new_count[-1]
            # Remove all -1
            new_count.pop(-1)

        age_count = new_count.copy()

    total_amount = 0
    for key, val in age_count.items():
        total_amount += val

    print("total of {} fish after {} days".format(total_amount, day + 1))


print("=" * 40, " PART ONE ", "=" * 40)

with open("day06\day06_input.txt", "r") as f:
    age_str = f.read()
    fish_age_p1 = [int(x) for x in age_str.strip("\n").split(",")]
    fish_age_p2 = fish_age_p1.copy()

get_fish_population(18, fish_age_p1)

print("=" * 40, " PART TWO ", "=" * 40)
# start_time = timeit.default_timer()

print(
    f'Time = {timeit.timeit("get_fish_population_efficient(256, fish_age_p2)", globals=locals(), number=1000)/1000}s'
)

# get_fish_population_efficient(256, fish_age_p2)
# stop_time = timeit.default_timer()
# print("execution time: {} seconds".format(stop_time - start_time))
print("=" * 40, "    END   ", "=" * 40)
