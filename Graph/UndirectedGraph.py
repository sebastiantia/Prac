def buildGraph(edges):
    graph = {}

    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def hasPath(visited, graph, src, dest):
    if src in visited: return False
    visited.add(src)

    if src == dest:
        return True
    for neighbor in graph[src]:
        if hasPath(visited, graph, neighbor, dest) == True:
            return True

    return False


if __name__ == "__main__":
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

    graph = buildGraph(edges)
    visited = set()
    print(hasPath(visited, graph, "i", "k"))
