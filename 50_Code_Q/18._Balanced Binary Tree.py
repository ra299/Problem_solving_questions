class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def findHeight(root):
    if (
        root is None
    ) : return False

    return max(
        findHeight(root.left),
        findHeight(root.left)
    ) + 1

def isBalanced(root):
    if(
        root == None
    ) : return False

    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)

    if (
        abs(leftHeight - rightHeight) <= 1 
        and check(root.left) is True
        and check(root.right) is True
    ): return True

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
