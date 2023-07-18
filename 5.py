def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
end = 'F'
paths = find_paths(graph, start, end)
print("Все пути от вершины", start, "до вершины", end, ":")
for path in paths:
    print(path)
