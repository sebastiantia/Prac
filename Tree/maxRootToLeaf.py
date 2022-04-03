class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def maxRootToLeaf(val):

        left, right = 0, 0

        if val.left != None:
            left = Node.maxRootToLeaf(val.left)
        if val.right != None:
            right = Node.maxRootToLeaf(val.right)

        return val.val + max(left, right)


    


if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(1)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(Node.maxRootToLeaf(a))