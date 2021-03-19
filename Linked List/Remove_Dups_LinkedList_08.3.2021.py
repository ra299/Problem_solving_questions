class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_Linked_List(self):
        temp = self.head
        while(temp):
            print(temp.data, end= " ")
            temp = temp.next

    def remove_dups(self, head):

        if (self.head is None or self.head.next is None):
            return head

        hash = set()
        current = head
        hash.add(self.head.data)

        while(current.next is not None):
            if(current.next.data in hash):
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head

        # without buffer

        # def removeDuplicates(self):
        # temp = self.head
        # if temp is None:
        #     return
        # while temp.next is not None:
        #     if temp.data == temp.next.data:
        #         new = temp.next.next
        #         temp.next = None
        #         temp.next = new
        #     else:
        #         temp = temp.next
        # return self.head

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    llist.print_Linked_List()
    llist.remove_dups(llist.head)
    print("\n")
    llist.print_Linked_List()
