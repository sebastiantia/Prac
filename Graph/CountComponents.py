

def connectedComponentCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(visited, graph, node) == True: count += 1
    return count


def explore(visited, graph, node):
    if node in visited: return False
    visited.add(node)    

    for neighbor in graph[node]:
        explore(visited, graph, neighbor)

    
    return True #Explored all possible neighbors; meaning you explored entire component
    

if __name__ == "__main__":
    graph = {
        0: [0,1,5],
        1: [0],
        2:[3,4],
        3:[2,4],
        4:[3,2],
        5:[0,8],
        8:[0,5]
    }
    print(connectedComponentCount(graph ))
