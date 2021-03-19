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

    def nth_to_last(self,head, k):
        p1 = head
        p2 = head
        for i in range(k):
            if(p1 == None):
                return None
            p1 = p1.next
        while(p1 != None):
            p1 = p1.next
            p2 = p2.next
        return p2

if __name__ == "__main__":

    l_List = LinkList()
    l_List.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    l_List.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    l_List.print_list()
    print(l_List.nth_to_last(l_List.head, 4))
    
