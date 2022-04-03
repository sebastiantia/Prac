#graph is ACYCLIC (no cycles)

# def dfsRecursvie(graph, src, dest):
#     if src == dest:
#         return True
#     for neighbor in graph[src]:
#         if dfsRecursvie(graph, neighbor, dest) == True:
#             return True
#     return False



def bfs(graph, src, dest):
    queue = [ src ]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def recursive(graph, src, dest):
    if src == dest:
        return True
    for neighbor in graph[src]:
        if recursive(graph, neighbor, dest) == True:
            return True
    
    return False
        
    

if __name__ == "__main__":
    graph = {
        "f":["g","i"],
        "g":["h"],
        "h":[],
        "i":["k","g"],
        "j":["i"],
        "k":[]
    }

    print(recursive(graph, "j", "f"))