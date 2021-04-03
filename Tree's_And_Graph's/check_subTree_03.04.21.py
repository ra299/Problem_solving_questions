class Node:
    def __init__(self,key):
        self.data = key
        self.left = self.right = None

def are_Indentical(root1, root2):
    if root1 and root2 is None:
        return True
    if root1 or root2 is None:
        return False

    return(
        root1.data == root2.data and are_Indentical(root1.left, root2.left) and are_Indentical(roo1.right , root2.right)
        )

def is_checked(T, S):
    if S is None:
        return True

    if T is None:
        return False

    if are_Indentical(T, S):
        return True

    return is_checked(T.left, S) or is_checked(T.right, S)

if __name__ == "__main__":
    """ TREE 1
     Construct the following tree
              26
            /   \
          10     3
        /    \     \
      4      6      3
       \
        30
    """
  
    T = Node(26)
    T.right = Node(3)
    T.right.right  = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)
    
    """ TREE 2
        Construct the following tree
            10
            /    \
        4      6
        \
            30
        """
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)
    
    if is_checked(T, S):
        print("Tree 2 is subtree of Tree 1")
    else :
        print("Tree 2 is not a subtree of Tree 1")