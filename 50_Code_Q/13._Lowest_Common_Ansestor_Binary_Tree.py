class Node:
    def __init__(self, data):
        self.key = data
        self.left = self.right = None

def find_path(root, path, k):
    if root == None:
        return False
    
    path.append(root.key)

    if root.key == k:
        return True

    if  (
            (
                root.left != None and find_path(root.left, path, k)
            ) or (
                root.right != None and find_path(root.right, path, k)
            )
        ) : return True
    path.pop()
    return False

def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if(
        not find_path(root, path1, n1) 
            or 
        not find_path(root, path2, n2)
    ) : return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if(
            path1[i] != path2[i]
        ): break
        i+=1
    return path1[i-1]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,)))
    print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
    print("LCA(3, 4) = %d" %(findLCA(root,3,4)))
    print("LCA(2, 4) = %d" %(findLCA(root,2, 4)))
    