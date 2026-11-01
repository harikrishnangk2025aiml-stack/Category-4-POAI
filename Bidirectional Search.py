def bidirectional(graph, start, goal):
    q1 = [start]
    q2 = [goal]
    visited1 = [start]
    visited2 = [goal]
    while q1 and q2:
        a = q1.pop(0)
        b = q2.pop(0)
        if a in visited2 or b in visited1:
            print("Path Found")
            return
        for i in graph[a]:
            if i not in visited1:
                visited1.append(i)
                q1.append(i)
        for i in graph[b]:
            if i not in visited2:
                visited2.append(i)
                q2.append(i)
    print("Path Not Found")
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}
bidirectional(graph, 'A', 'E')