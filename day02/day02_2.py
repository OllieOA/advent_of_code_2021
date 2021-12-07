with open("day02_1_input.txt", "r") as f:
    measurements_str = f.readlines()
    measurements = [(m.split(" ")[0], int(m.split(" ")[1])) for m in measurements_str]

pos_and_aim = [0, 0, 0]

dirs = {
    "forward": [1, 0, 0],
    "down": [0, 0, 1],
    "up": [0, 0, -1]
}

for measurement in measurements:
    modifier = [x * measurement[1] for x in dirs[measurement[0]]]

    if measurement[0] == "forward":
        # Handle special case
        modifier[1] = pos_and_aim[2] * measurement[1]
    
    new_pos = [x + y for x, y in zip(pos_and_aim, modifier)]
    pos_and_aim = new_pos


print("resultant pos: {}".format(pos_and_aim))
print("resultant ans: {}".format(pos_and_aim[0] * pos_and_aim[1]))