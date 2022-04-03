from numpy import Infinity


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
    def minimum(val):
        
        mini = 10000000
        stack = [ val ]

        while len(stack) > 0:
            current = stack.pop()

            mini = min(current.val, mini)

            if current.left != None:
                stack.append(current.left)

            if current.right != None:
                stack.append(current.right)

        return mini 

    
    def recursive(val):

        l ,r = 1000000, 1000000

        if val.left != None:
            l = Node.recursive(val.left)

        if val.right != None:
            r  = Node.recursive(val.right)

        return min(l, r, val.val)

        #RECURSION (THINK BASE CASE)





if __name__ == "__main__":
    a = Node(20)
    b = Node(11)
    c = Node(9)
    d = Node(10)
    e = Node(21)
    f = Node(5)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f


    print(Node.recursive(a))