import time
class Node: 
 
    def __init__(self, data): 
        self.data = data 
        self.next = None
 
class LinkedList: 
 
    def __init__(self): 
        self.head = None
 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
 
    def deleteNode(self, key): 
         
        temp = self.head 
 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
 
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
 
        # if(temp == None): 
        #     return
 
        prev.next = temp.next
 
        temp = None
 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (" %d" %(temp.data)), 
            temp = temp.next
 
 
llist = LinkedList() 
llist.push(11) 
llist.push(14) 
llist.push(16) 
llist.push(18) 
llist.push(20) 
 
print ("Created Linked List: ")
llist.printList()
time.sleep(3) 
llist.deleteNode(16) 
print ("\nLinked List after Deletion of 1:")
llist.printList() 