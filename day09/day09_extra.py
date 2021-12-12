import numpy as np
import timeit


def convolution2d(image, kernel):
    m, n = kernel.shape
    if m == n:
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y, x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i : i + m, j : j + m] * kernel)

    return new_image


heightmap = []

with open("day09\day09_input.txt", "r") as f:
    lines = f.readlines()

start_time = timeit.default_timer()

for line in lines:
    heightmap.append([int(x) for x in line.strip("\n")])

heightmap = np.array(heightmap)

padded_heightmap = np.pad(heightmap, (1,), mode="constant", constant_values=(5))
# kernel1 = np.array([[-1, 0, -1], [-2, 0, -2], [-1, 0, -1]])
kernel1 = np.array([[0, -1, 0], [0, 1, 0], [0, -1, 0]])
kernel2 = kernel1.T
# kernel1 = np.array([[0, -1, 0], [0, 1, 0], [0, -1, 0]])
# kernel2 = kernel1.T
# kernel3 = np.array([[0, 0, 0], [0, 1, 0], [0, -1, 0]])
# kernel4 = kernel3.T

kernels = [kernel1]  # , kernel2]  # , kernel3, kernel4]

convolutions = []
for kernel in kernels:
    conv = convolution2d(padded_heightmap, kernel)
    convolutions.append(conv)

convolutions = np.array(convolutions)

lowest_points = []
for i in range(convolutions.shape[1]):
    for j in range(convolutions.shape[2]):
        if all(x < 1 for x in convolutions[:, i, j]):
            lowest_points.append((i, j))


total_sum = 0
for point in lowest_points:
    total_sum += heightmap[point] + 1

stop_time = timeit.default_timer()
print("execution time: {} seconds".format(stop_time - start_time))

print(f"final result: {total_sum}")
