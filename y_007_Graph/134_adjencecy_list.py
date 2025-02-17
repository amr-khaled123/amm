def adj_list(n, edge):
    graph = [[]for i in range(n)]
    for e in edge:
        a = e[0]
        b = e[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


n = 5
edge = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3)]

graph = adj_list(n, edge)
