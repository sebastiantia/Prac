class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
    def depth(self):
        stack = [ self ]

        depth = 0

        while len(stack) > 0:
            current = stack.pop()
            
            
            
            

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(2)
    e = Node(4)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    
