class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None

    def add(self,val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return("({val}) ".format(val=self.val) + str(self.next))

class BinaryTrees:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return("<Binary Tree (val is {val}). \n\tleft is {left} \n\tright is {right}>".format(val=self.val, left=self.left, right=self.right))        

def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight

def tree_to_linked_Lists(tree, lists = {}, d = None):
    if d == None:
        d = depth(tree)
    if lists.get(d) == None:
        lists[d] = LinkedList(tree.val)
    else:
        lists[d].add(tree.val)
        if d == 1:
            return lists
    if tree.left != None:
        lists = tree_to_linked_Lists(tree.left, lists, d-1)
    if tree.right != None:
        lists = tree_to_linked_Lists(tree.right, lists, d-1)
    return lists


if __name__ == "__main__":
    b_tree = BinaryTrees(1)
    b_tree.left = BinaryTrees(2)
    b_tree.right = BinaryTrees(3)
    b_tree.left.left = BinaryTrees(4)
    b_tree.left.right = BinaryTrees(5)
    b_tree.right.right = BinaryTrees(7)
    b_tree.right.left = BinaryTrees(6)

    a = tree_to_linked_Lists(b_tree)

    # def display_Linked_List(linked_list):
    #     current = linked_list.val
    #     while current.next != None:
    #         print(current.val, end = " ")
    #         current = current.next

    # display_Linked_List(a)

    for i in a:
        print(i)
    