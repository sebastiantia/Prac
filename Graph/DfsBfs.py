def dfs(graph, node):  # function for dfs
    stack = [node]
    while len(stack) > 0:
        print(stack)
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

def dfsRecursion(graph, node):
    print(node)
    for neighbor in graph[node]:
        dfsRecursion(graph, neighbor)


def bfs(graph, node):
    queue = [ node ]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)



if __name__ == "__main__":
    graph = {"a": ["c","b"],
             "b": ["d"],
             "c": ["e"],
             "d": ["f"],
             "e": [],
             "f": []}

    bfs(graph, "a")
