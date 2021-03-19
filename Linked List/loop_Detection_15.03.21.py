class Node:    
  def __init__(self,data):    
    self.data = data
    self.next = None
     
class CreateList:    
  
  def __init__(self):    
    self.head = Node(None)
    self.tail = Node(None) 
    self.head.next = self.tail   
    self.tail.next = self.head
        
  
  def add(self,data):    

    newNode = Node(data)
    if self.head.data is None:
      self.head = newNode
      self.tail = newNode
      newNode.next = self.head 
    else:
      self.tail.next = newNode
      self.tail = newNode
      self.tail.next = self.head
     
  
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty") 
      return;    
    else:    
        print("Nodes of the circular linked list: ");    
        
        print(current.data),    
        while(current.next != self.head):    
            current = current.next;    
            print(current.data),    
     
  def findingBeginning(self):
        fast = self.head
        slow = self.head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(fast == slow):
                break
        if(fast == None or fast.next == None):
            return None

        slow = self.head
        while(slow == fast):
            slow = slow.next
            fast = fast.next
        return fast
   
if __name__ == "__main__":
    cl = CreateList()    
    cl.add("a")
    cl.add("b")
    cl.add("c")
    cl.add("d")
    cl.add("e")
    cl.add("c")

    cl.display();  
    a = cl.findingBeginning()
    print("After this")
    print(a)
