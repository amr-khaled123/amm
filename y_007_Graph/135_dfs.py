def adj_list(n, edge):
    graph = [[]for i in range(n)]
    for e in edge:
        a = e[0]
        b = e[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(graph, visted, currentnode):
    visted[currentnode] = True
    print(currentnode)
    for node in graph[currentnode]:
        if visted[node]:
            continue
        else:
            dfs(graph, visted, node)


n = 5
edge = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3)]
graph = adj_list(n, edge)

visted = [False for i in range(n)]
dfs(graph, visted, 2)
