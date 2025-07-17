graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B']),
    'F': set(['C', 'G']),
    'G': set(['F', 'H', 'I']),
    'H': set(['G', 'I']),
    'I': set(['G', 'H', 'J', 'K']),
    'J': set(['I']),
    'K': set(['I', 'L', 'M']),
    'L': set(['K']),
    'M': set(['K'])
}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'A', 'M')))