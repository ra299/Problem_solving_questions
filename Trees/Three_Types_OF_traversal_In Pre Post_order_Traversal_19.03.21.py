#                                                         1

#                                    2                                             3

#                   4                             5
# the graph

#----------------------------------------------------------------------------------------------------
# InOrder_Traversal [Left, Root, Right] ----> 4 , 2 , 5 , 1 , 3
# PreOrder_Traversal [Root, Left, Right] ------> 1 , 2  , 4 , 5 , 3 || Breadth First or Level Order Traversal : 1 2 3 4 5 [ Same ]
# PostOrder_Traversal [Left, Right, Root] -------> 4 , 5 , 2 , 3 , 1

count = [10]
class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def print_2d_Tree(root, space):
    if root == None:
        return
    space +=count[0]
    print_2d_Tree(root.right, space)
    print()
    for i in range(count[0], space):
        print(end = " ")
    print(root.data)
    print_2d_Tree(root.left, space)

def print_tree(root):
    print_2d_Tree(root,0)

def inOrder_Traversal(root):
    if root == None:
        return
    else:
        inOrder_Traversal(root.left)
        print(root.data)
        inOrder_Traversal(root.right)

def preOrder_Traversal(root):
    if root == None:
        return
    else:
        print(root.data)
        preOrder_Traversal(root.left)
        preOrder_Traversal(root.right)

def postOrder_Traversal(root):
    if root == None:
        return
    else:
        preOrder_Traversal(root.left)
        preOrder_Traversal(root.right)
        print(root.data)

if __name__ == "__main__":
    root = Tree(1) 
    root.left      = Tree(2) 
    root.right     = Tree(3) 
    root.left.left  = Tree(4) 
    root.left.right  = Tree(5) 
    print_tree(root)
    print("\n")
    print("Preorder traversal of binary tree is")
    preOrder_Traversal(root) 
    
    print("\nInorder traversal of binary tree is")
    inOrder_Traversal(root) 
    
    print("\nPostorder traversal of binary tree is")
    postOrder_Traversal(root)
