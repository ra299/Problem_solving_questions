class Node:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

def maxPathLenth(root, prev_val, prev_len):
    if(
        root == None
    ) : return prev_len

    currentVal = root.val
    if(currentVal == prev_val +1):
        return max(
            maxPathLenth(root.left, currentVal, prev_len+1),
            maxPathLenth(root.right, currentVal, prev_len+1)
        )
    
    newPath = max(
        maxPathLenth(root.left, currentVal, 1),
        maxPathLenth(root.right, currentVal, 1)
    )
    return max(
        prev_len, newPath
    )

def maxConsecutivePathLength(root):
      
    if root is None:
        return 0 

    return maxPathLenth(root, root.val -1 , 0)
  

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(13)
    root.left.right = Node(12)
    root.right.left = Node(13)
    root.right.right = Node(8)

    print(maxConsecutivePathLength(root))