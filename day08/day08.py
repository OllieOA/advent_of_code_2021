from os import linesep


print("=" * 40, " PART ONE ", "=" * 40)

with open("day08/day08_input.txt", "r") as f:
    lines = f.readlines()

actual_pos = ["A", "B", "C", "D", "E", "F", "G"]

problems = []

for line in lines:
    input_str, output_str = line.split("|")
    input_list = ["".join(sorted(x)) for x in input_str.split(" ") if x != ""]
    output_list = [
        "".join(sorted(x.strip("\n"))) for x in output_str.split(" ") if x != ""
    ]

    problems.append((input_list, output_list))

valid_num = 0
valid_lens = [2, 4, 3, 7]
for problem in problems:
    curr_output = problem[1]

    valid_num += sum([1 for x in curr_output if len(x) in valid_lens])

print("Final answer: ", valid_num)

print("=" * 40, " PART TWO ", "=" * 40)

""" This is absolutely dreadful manual logic. Nothing is clever about this
"""

""" Actual segments
 AAAA
B    C
B    C
 DDDD
E    F
E    F
 GGGG

"""
digit_lens = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
digit_compositions = {
    0: set(["A", "B", "C", "E", "F", "G"]),
    1: set(["C", "F"]),
    2: set(["A", "C", "D", "E", "G"]),
    3: set(["A", "C", "D", "F", "G"]),
    4: set(["B", "C", "D", "F"]),
    5: set(["A", "B", "D", "F", "G"]),
    6: set(["A", "B", "D", "F", "E", "G"]),
    7: set(["A", "C", "F"]),
    8: set(["A", "B", "C", "D", "E", "F", "G"]),
    9: set(["A", "B", "C", "D", "F", "G"]),
}

output_sum = 0

for problem in problems:
    curr_input = problem[0]
    curr_output = problem[1]
    solution = [-1] * len(curr_input)

    segment_assignments_forward = {}
    segment_assignments_reverse = {}
    number_assignments_forward = {}
    number_assignments_reverse = {}

    # Get count of segments for deduction
    full_input_str = "".join(curr_input)
    segment_counts = dict((x, full_input_str.count(x)) for x in set(full_input_str))

    for key, val in segment_counts.items():
        if val == 4:
            segment_assignments_forward.update({key: "E"})
            segment_assignments_reverse.update({"E": key})
        elif val == 6:
            segment_assignments_forward.update({key: "B"})
            segment_assignments_reverse.update({"B": key})
        elif val == 9:
            segment_assignments_forward.update({key: "F"})
            segment_assignments_reverse.update({"F": key})

    for prob in curr_input:
        if len(digit_lens[len(prob)]) == 1:
            number_assignments_forward.update({prob: digit_lens[len(prob)][0]})
            number_assignments_reverse.update({digit_lens[len(prob)][0]: prob})

    # Resolve 1's top line
    curr_1 = number_assignments_reverse[1]
    curr_bottom_right = segment_assignments_reverse["F"]
    curr_top_right = list(set(curr_1).difference(set(curr_bottom_right)))[0]

    segment_assignments_reverse.update({"C": curr_top_right})
    segment_assignments_forward.update({curr_top_right: "C"})

    # Resolve top line from 7
    curr_1 = number_assignments_reverse[1]
    curr_7 = number_assignments_reverse[7]
    curr_top = list(set(curr_7).difference(curr_1))[0]

    segment_assignments_reverse.update({"A": curr_top})
    segment_assignments_forward.update({curr_top: "A"})

    # Resolve the middle and top left from 4
    curr_4 = number_assignments_reverse[4]
    middle_and_top_right = list(set(curr_4).difference(set(curr_1)))
    for element in middle_and_top_right:
        if segment_counts[element] == 7:
            curr_middle = element

    segment_assignments_reverse.update({"D": curr_middle})
    segment_assignments_forward.update({curr_middle: "D"})

    # Resolve bottom
    for single_char in number_assignments_reverse[8]:
        if single_char not in segment_assignments_forward.keys():
            curr_bottom = single_char
            segment_assignments_reverse.update({"G": single_char})
            segment_assignments_forward.update({single_char: "G"})

    # Now resolve numbers
    for number_str in curr_input:
        if number_str not in number_assignments_forward.keys():
            number_set = set([])

            for single_char in number_str:
                number_set.add(segment_assignments_forward[single_char])

            for num, relevant_set in digit_compositions.items():
                if number_set == relevant_set:
                    number_assignments_forward.update({number_str: num})
                    number_assignments_reverse.update({num: number_str})

    curr_int = ""
    for num_str in curr_output:
        curr_int += str(number_assignments_forward[num_str])

    output_sum += int(curr_int)

print(f"Final result: {output_sum}")

print("=" * 40, "    END   ", "=" * 40)
