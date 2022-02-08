from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def maxLevelSum(root):
    # Base case
    if (root == None):
        return 0

    result1 = root.data
    q = deque()
    q.append(root)

    while (len(q) > 0):
        count = len(q)
        sum = 0
        while (count > 0):
            temp = q.popleft()
            sum = sum + temp.data
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
            count -= 1
        result1 = max(sum, result1)
    return result1

def minLevelSum(root):
    # Base case
    if (root == None):
        return 0

    result2 = root.data
    q = deque()
    q.append(root)

    while (len(q) > 0):
        count = len(q)
        sum = 0
        while (count > 0):
            temp = q.popleft()
            sum = sum + temp.data
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
            count -= 1
        result2 = min(sum, result2)
    return result2

if __name__ == '__main__':
    root = Node(30)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    # Constructed Binary tree is:
    #              30
    #            /   \
    #          2      3
    #        /  \      \
    #       40    50      8
    #                 /   \
    #                6     7
    print("Output: ", maxLevelSum(root)+minLevelSum(root))