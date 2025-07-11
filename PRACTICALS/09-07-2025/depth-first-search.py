graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E', 'G']),
    'G': set(['F', 'H', 'I']),
    'H': set(['G', 'I']),
    'I': set(['G', 'H', 'J', 'K']),
    'J': set(['I']),
    'K': set(['I', 'L', 'M']),
    'L': set(['K']),
    'M': set(['K'])
}

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited

print(dfs(graph, 'A'))