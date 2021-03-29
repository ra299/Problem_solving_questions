class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1 

def is_blanced(root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <=1) and is_blanced.left is True and is_blanced(root.right).right is True:
        return True
    return False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    if isBalanced(root):
        print("Tree is balanced")
    else:
        print("Tree is not balanced")


# ----- 2nd Approch ----- #

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Height:
#     def __init__(self):
#         self.height = 0

# def check_blns(root):
#     lh = Height()
#     rh = Height()

#     if root is None:
#         return True
    
#     l = check_blns(root.left)
#     r = check_blns(root.right)

#     if (lh.height - rh.height) <= 1:
#         return l and r
#     return False


# if __name__ == "__main__":
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.left.left.left = Node(7)

#     if (check_blns(root)):
#         print("ok")
#     else:
#         print("not ok")
