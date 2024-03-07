import math
class Node:
    def __init__(self, val=0, left=None, right=None, size=0):
        self.val = val
        self.left = left
        self.right = right
        self.size = size
l = [2, 3, 4, 5, 6, 7]

#Problem 1
def preOrder(root):
    curr = root
    for num in l:
        curr.left = Node(num)
        curr = curr.left

#Problem 2
def postOrder(root):
    curr = root
    for num in reversed(l):
        curr.left = Node(num)
        curr = curr.left


#Problem 3
def computeSize(root):
    if root:
        sizeLeft = computeSize(root.left)
        sizeRight = computeSize(root.right)
        root.size = sizeLeft + sizeRight + 1
        return root.size

    return 0


#Problem 4
def printLevel(root, k):
    if root is None:
        return 
    count = 0
    queue = [root]
    
    while len(queue) != 0:
        for i in range(len(queue)):
            ele = queue.pop(0)
            if ele:
                if count == k:
                    print(ele.val, end=" ")
                queue.append(ele.left)
                queue.append(ele.right)
        count += 1

#Problem 5
l = [False]
re = [Node(0)]
def findPreOrder(root, u):
    if root:
        if l[0]:
            re[0] = root
            l[0] = False
        if root == u:
            l[0] = True
            print(root.val)
        findPreOrder(root.left, u)
        findPreOrder(root.right, u)




def printLevelOrder(root):
 
    # Base Case
    if root is None:
        return
 
    # Create an empty queue
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
 
        # Print front of queue and
        # remove it from queue
        print(queue[0].val, queue[0].size, end="\n")
        node = queue.pop(0)
 
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)




a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(17)
f = Node(12)
a.left = b
a.right = c
b.left = d
c.right = e
c.left = f
findPreOrder(a,c)
print(re[0].val)
