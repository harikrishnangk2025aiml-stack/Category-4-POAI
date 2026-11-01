def dls(graph, start, limit, depth=0):
    print(start, end=" ")

    if depth == limit:
        return
    for i in graph[start]:
        dls(graph, i, limit, depth + 1)
graph = {
    'Grandfather': ['Father', 'Uncle'],
    'Father': ['Son'],
    'Uncle': ['Cousin'],
    'Son': [],
    'Cousin': []
}
dls(graph, 'Grandfather', 2)