class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def displayList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next

    def splitUp(self, list1, list2):

        firstPointer = self.head
        secondPonter = firstPointer.next

        while( firstPointer is not None and secondPonter is not None and firstPointer.next is not None ):

            self.splitNode(list1, firstPointer)
            self.splitNode(list2, secondPonter)

            firstPointer = firstPointer.next.next

            if firstPointer is None:
                break
            secondPonter = firstPointer.next

    def splitNode(self,storage, pointer):
        newNode = Node(pointer.data)
        if storage.head is None:
            storage.head = newNode
        else:
            newNode.next = storage.head
            storage.head = newNode

if __name__ == "__main__":
    llist = LinkedList()
    splitList_1 = LinkedList()
    splitList_2 = LinkedList()
     
    # Created linked list will be
    # 0->1->2->3->4->5
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(0)
    llist.push(110)
     
    # llist.splitUp(splitList_1, splitList_2)
     
    print("Original Linked List: ")
    llist.displayList()
    print("\n")
    print(llist.head.data)
     
    # print("Resultant Linked List 'a' : ")
    # splitList_1.displayList()
    # print("\n")
     
    # print("Resultant Linked List 'b' : ")
    # splitList_2.displayList()