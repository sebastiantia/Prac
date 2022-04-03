class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self):
        stack = [ self ]

        sum = 0

        while len(stack) > 0:
            current = stack.pop()
            sum += current.val

            if current.right != None:
                stack.append(current.right)
            
            if current.left != None:
                stack.append(current.left)

        return sum

    def recursive(self, result):
        if self == None:
            return 0

        left = 0 
        right = 0

        if self.left != None:
            left = Node.recursive(self.left, result)

        if self.right != None:
            right = Node.recursive(self.right, result)

        return left + right + self.val
            

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

    result = 0 

    print(Node.recursive(f, result))



