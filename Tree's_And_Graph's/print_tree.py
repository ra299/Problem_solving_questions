COUNT = [10] 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def print2DUtil(root, space) :
    
    if (root == None) :
        return
  
    space += COUNT[0]
  
    print2DUtil(root.right, space)
    
    print() 
    for i in range(COUNT[0], space):
        print(end = " ") 
    print(root.data) 
      
    print2DUtil(root.left, space) 
  
def print2D(root) :
    print2DUtil(root, 0) 

def height(root):
    if(
        root is None
    ) : return False

    return max(
        height(root.left),
        height(root.right)
    ) + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    print2D(root)
    # print(height(root))