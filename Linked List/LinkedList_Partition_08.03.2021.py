class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def partition(node, x):
    head = node
    tail = node

    while(node != None):
        next = node.next
        if(node.data < x):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head


if __name__ == "__main__":

    l_List = LinkList()
    l_List.head = Node(1)
    second = Node(16)
    third = Node(2)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(10)
    seventh = Node(1)

    l_List.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    l_List.print_list()
    print("\n")
    partition(l_List.head, 5)
    l_List.print_list()