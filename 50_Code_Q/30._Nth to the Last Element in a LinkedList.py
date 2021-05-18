class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def displayList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next

    def findLenth(self):
        lenth = 0
        temp = self.head
        while(temp):
            lenth+=1
            temp = temp.next
        return lenth

    def print_upt_n(self,n):
        if(n > self.findLenth()):
            return False
        temp = self.head
        while(temp.next.data != n):
            temp = temp.next
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.displayList()
    llist.print_upt_n(4)