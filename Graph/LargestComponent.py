


def traversaldfs(visited, graph, node):
    if node in visited: return 0
    size = 1
    visited.add(node)

    for neighbor in graph[node]:
        size += traversaldfs(visited,  graph, neighbor)

    return size

if __name__ == "__main__":
    graph = {
        0:[8,1,5],
        1:[0],
        2:[3,4],
        3:[2,4],
        4:[3,2],
        5:[0,8],
        8:[0,5]
    }

    visited = set()
    biggest = 0
    for node in graph:
        if node not in visited:
            count = traversaldfs(visited, graph, node)
            if count > biggest:
                biggest = count

    
    print(biggest)
