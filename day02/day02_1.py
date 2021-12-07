with open("day02_1_input.txt", "r") as f:
    measurements_str = f.readlines()
    measurements = [(m.split(" ")[0], float(m.split(" ")[1])) for m in measurements_str]

pos = [0, 0]

dirs = {
    "forward": [1., 0.],
    "down": [0., 1.],
    "up": [0., -1.]
}

for measurement in measurements:
    modifier = [x * measurement[1] for x in dirs[measurement[0]]]
    print("modifier is {}".format(modifier))
    new_pos = [x + y for x, y in zip(pos, modifier)]
    pos = new_pos

print("resultant pos: {}".format(pos))
print("resultant ans: {}".format(pos[0] * pos[1]))