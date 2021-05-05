int_max = 100
int_min = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node):    
    return isBST_(node, int_min, int_max)   

def isBST_(node, mini, maxi):   

    if(
        node is None    
    ) : return True
    
    if (
        node.data < mini or node.data > maxi    
    ) : return False

    return (isBST_(node.left, mini, node.data-1) and    
        isBST_(node.right, node.data+1, maxi))

if __name__ == "__main__":
    node = Node(8)  
    node.left = Node(5) 
    node.right = Node(12)    
    node.left.left = Node(4)    
    node.left.right = Node(10)   
    node.right.left = Node(9)
    node.right.right = Node(16)

    # if (isBST(node)):   
    #     print("Is BST")
    # else:
    #     print("Not a BST")

    print(isBST(node))