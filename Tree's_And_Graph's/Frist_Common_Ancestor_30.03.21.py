class FCA:
    def __init__(self,key):
        self.key = key
        self.left = self.right = None

def find_CA(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = find_CA(root.left, n1, n2)
    right_lca = find_CA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

if __name__ == "__main__":
    root = FCA(1)
    root.left = FCA(2)
    root.right = FCA(3)
    root.left.left = FCA(4)
    root.left.right = FCA(5)
    root.right.left = FCA(6)
    root.right.right = FCA(7)
    print("LCA(2,4) = ", find_CA(root, 2, 4).key)
    print("LCA(4,5) = ", find_CA(root, 4, 5).key)
    print("LCA(4,6) = ", find_CA(root, 4, 6).key)
    print("LCA(3,4) = ", find_CA(root, 3, 4).key)