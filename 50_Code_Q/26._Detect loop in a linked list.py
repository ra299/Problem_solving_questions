class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def display_(self):
        current = self.head
        while(current):
            print(current.data," --> ", end = "")
            current = current.next
    def checkLoop(self):
        temp = self.head
        s = set()
        while(temp):
            if(temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    llist.push(8)

    llist.display_()

    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    print("linked list head--",llist.head.data)

    if(llist.checkLoop()):
        print("\n Loop found")
    else:
        print("Dont have any Loop")