def dfs(graph, start, visited=[]):
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        for i in graph[start]:
            dfs(graph, i, visited)
graph = {
    'Folder': ['Images', 'Documents'],
    'Images': ['Photos'],
    'Documents': ['PDF'],
    'Photos': [],
    'PDF': []
}
dfs(graph, 'Folder')