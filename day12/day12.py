print("=" * 40, " PART ONE ", "=" * 40)


def dfs(graph, start, dest):
    valid_paths = []
    path_list = [[start]]

    while path_list:
        path = path_list.pop()

        if path[-1] == dest:
            valid_paths.append(path)

        else:
            for node in graph[path[-1]]:
                if node not in path or node.isupper():
                    new_path = path + [node]
                    path_list.append(new_path)

    return valid_paths


def dfs_double(graph, start, dest):
    valid_paths = []

    double_visit = [
        cave
        for cave in graph.keys()
        if cave != "end" and cave != "start" and cave.islower()
    ]
    print(f"Double visit cave options: {double_visit}")

    for double_cave in double_visit:
        path_list = [[start]]
        while path_list:
            path = path_list.pop()

            if path[-1] == dest:
                valid_paths.append(path)

            else:
                for node in graph[path[-1]]:
                    if node not in path or node.isupper():
                        new_path = path + [node]
                        path_list.append(new_path)
                    elif node == double_cave and node in path:
                        if path.count(node) == 1:
                            new_path = path + [node]
                            path_list.append(new_path)

    return valid_paths


# Generate graph
with open("day12/day12_input.txt", "r") as f:
    lines = f.readlines()


# Initialise graph
graph = {"start": [], "end": []}

for line in lines:
    node1, node2 = line.strip("\n").split("-")

    if node1 not in graph.keys():
        graph[node1] = []
    if node2 not in graph.keys():
        graph[node2] = []

    if node2 == "end":
        graph[node1].append(node2)
    elif node1 == "start":
        graph[node1].append(node2)
    else:
        graph[node1].append(node2)
        graph[node2].append(node1)

paths = dfs(graph, "start", "end")

print(f"Final answer: {len(paths)}")

print("=" * 40, " PART TWO ", "=" * 40)

paths_p2 = dfs_double(graph, "start", "end")
path_str = []
for path in paths_p2:
    path_str.append(",".join(path))

path_set = set(path_str)
print(f"Final answer {len(path_set)}")


print("=" * 40, "   END    ", "=" * 40)
