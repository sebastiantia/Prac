
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(root):
        if root == None:
            return 
        stack = [ root ]
        
        while len(stack) > 0:
            current = stack.pop()

            print(current.val)
            if current.left != None:
                stack.append(current.left)
            if current.right != None:
                stack.append(current.right)

    def dfsRecursive(root, result):
        if root == None:
            return []
        
        result.append(root.val)

        if root.left != None:
            Node.dfsRecursive(root.left, result)
        if root.right != None:
            Node.dfsRecursive(root.right, result)

        return result


    def bfs(root):
        if root == None:
            return
        result = []
        queue = [ root ]
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.val)

            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

        print(result)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    null = Node(None)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    # Node.bfs(a)
    result = []
    # print(Node.bfs(a))
    print(Node.dfsRecursive(a, result))

        
