class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bfs(self, value):

        if self == None:
            return False
        
        queue = [ self ]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.val == value:
                return True
            
            if current.left != None:
                queue.append(current.left)

            if current.right != None:
                queue.append(current.right)


        return False

    def recursive(self, value):

        if self == None:
            return False

        elif self.val == value:
            return True
        
        bool1 = False
        bool2 = False
        if self.left != None: 
            bool1 = Node.recursive(self.left, value)  
        if self.right != None:
            bool2 = Node.recursive(self.right, value)
        
        return bool1 or bool2

    

    



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

    print(Node.recursive(a, 'g'))
