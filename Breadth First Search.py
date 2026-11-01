def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for i in graph[node]:
                queue.append(i)
graph = {
    'Home': ['School', 'Park'],
    'School': ['Hospital'],
    'Park': ['Mall'],
    'Hospital': [],
    'Mall': []
}
bfs(graph, 'Home')