
from dis import dis


def bfs(graph, src, dest):
    queue = [ [src, 0] ] # 0 edges away from itself

    visited = set([ src ])

    while len(queue) > 0:
        current = queue.pop(0)
        [node, distance] = current
        
        if node == dest: return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

    return -1
    

if __name__=="__main__":
    edges = [
        ['w','x'],
        ['x','y'],
        ['z','y'],
        ['z','v'],
        ['w','v']
    ]
    graph = {}

    for edge in edges:
        [a,b] = edge
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    
    print(bfs(graph, 'w','z'))
    #find shortest path between source and dest with bfs

    
