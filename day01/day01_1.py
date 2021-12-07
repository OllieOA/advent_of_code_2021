with open("day01_1_input.txt", "r") as f:
    measurements = f.readlines()

num_increased = 0
num_decreased = 0

for i in range(len(measurements)):
    if i != 0:
        curr_measurement = float(measurements[i])
        prev_measurement = float(measurements[i-1])

        if curr_measurement >= prev_measurement:
            num_increased += 1
        else:
            num_decreased += 1
    
print("num_increased = {}".format(num_increased))
print("num_decreased = {}".format(num_decreased))
print("sum = {}".format(num_decreased + num_increased))