from os import remove


print("=" * 40, " PART ONE ", "=" * 40)

with open("day10/day10_input.txt", "r") as f:
    lines = f.readlines()

prison = []
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

incomplete_lines = []

for line in lines:
    corrupt = False
    curr_line = line.strip("\n")
    curr_list = [x for x in curr_line]
    new_pair = True

    while new_pair:
        new_pair = False

        for i in range(len(curr_list) - 1):
            if curr_list[i] in pairs.keys():
                if curr_list[i + 1] == pairs[curr_list[i]]:
                    new_pair = True
                    remove_pair = i

        if new_pair:
            curr_list.pop(remove_pair)
            curr_list.pop(remove_pair)

    condensed = "".join([x for x in curr_list])
    for i in range(len(condensed) - 1):
        if condensed[i] in pairs.keys() and condensed[i + 1] in pairs.values():
            if pairs[condensed[i]] != condensed[i + 1]:
                prison.append(condensed[i + 1])
                corrupt = True

    if not corrupt:
        incomplete_lines.append(condensed)

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
curr_score = 0

for inmate in prison:
    curr_score += scores[inmate]

print(f"final result: {curr_score}")

print("=" * 40, " PART TWO ", "=" * 40)

scores = []

close_values = {")": 1, "]": 2, "}": 3, ">": 4}

for line in incomplete_lines:
    completion_list = []
    for character in reversed(line):
        completion_list.append(pairs[character])
    completion_str = "".join(completion_list)

    total_score = 0
    for character in completion_str:
        total_score = total_score * 5 + close_values[character]

    scores.append(total_score)

ordered_scores = sorted(scores)
final_score = ordered_scores[(len(ordered_scores) - 1) // 2]

print(f"final result: {final_score}")


print("=" * 40, "    END   ", "=" * 40)
