class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def createArrayToBST(arr):

    if not arr:
        return False
    
    mid = (len(arr)) // 2 

    root = Node(arr[mid])
    root.left = createArrayToBST(arr[:mid])
    root.right = createArrayToBST(arr[mid+1:])

    return root

def preOrder(node):
    if not node:
        return

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7] 
    root = createArrayToBST(arr) 
    print("PreOrder Traversal of constructed BST ")
    preOrder(root) 
    