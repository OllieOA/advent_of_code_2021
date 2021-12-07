with open("day01_1_input.txt", "r") as f:
    measurements_str = f.readlines()
    measurements = [int(m) for m in measurements_str]

num_increased = 0
num_decreased = 0

for i in range(len(measurements) - 2):
    if i != 0:
        if i == 1:
            print("1. Checking {} sums to {}".format(measurements[i:i+3], sum(measurements[i:i+3])))
            print("2. Checking {} sums to {}".format(measurements[i-1:i+2], sum(measurements[i-1:i+2])))

        curr_sum = sum(measurements[i:i+3])
        prev_sum = sum(measurements[i-1:i+2])

        if curr_sum > prev_sum:
            num_increased += 1
        else:
            num_decreased += 1

        if i == 1:
            print("{}, {}".format(num_increased, num_decreased))
    
print("num_increased = {}".format(num_increased))
print("num_decreased = {}".format(num_decreased))
print("sum = {}".format(num_decreased + num_increased))