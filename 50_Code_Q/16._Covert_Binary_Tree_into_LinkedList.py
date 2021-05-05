class Node:
    def __init__(self):
        self.key = None
        self.left = self.right = None

def newNode(data):
    node = Node()
    node.key = data
    node.left = node.right= None
    return node

def inorder(root):
    if (
        root == None
    ) : return

    inorder(root.left)
    print(root.key, end = " ")
    inorder(root.right)

def converToLinkedList(root):
    if (
        root == None or
        root.left == None and
        root.right == None
    ) : return

    if (root.left != None):

        converToLinkedList(root.left)

        tempRight = root.right
        root.right = root.left
        root.left = None

        t = root.right
        while( t.right != None):
            t = t.right

        t.right = tempRight

    converToLinkedList(root.right)

if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(3)
    root.left.right = newNode(4)
    root.right.right = newNode(6)

    inorder(root)
    converToLinkedList(root)
    print("\n")
    inorder(root)