count = [10]
class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print2DTree(root, space):
    if root == None:
        return
    else:
        space +=count[0]
        print2DTree(root.right, space)
        print()
        for i in range(count[0], space):
            print(end = " ")
        print(root.val)
        print2DTree(root.left, space)

def print_2nd(root):
    print2DTree(root, 0)

if __name__ == "__main__":

    root = Tree(1)  
    root.left = Tree(2)  
    root.right = Tree(3)  
  
    root.left.left = Tree(4)  
    root.left.right = Tree(5)  
    root.right.left = Tree(6)  
    root.right.right = Tree(7)  
  
    root.left.left.left = Tree(8)  
    root.left.left.right = Tree(9)  
    root.left.right.left = Tree(10)  
    root.left.right.right = Tree(11)  
    root.right.left.left = Tree(12)  
    root.right.left.right = Tree(13)  
    root.right.right.left = Tree(14)  
    root.right.right.right = Tree(15) 

    print_2nd(root)