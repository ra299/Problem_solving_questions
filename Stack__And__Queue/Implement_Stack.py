class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
            
    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            pop_Node = self.head
            self.head = self.head.next
            pop_Node.next = None
            return pop_Node

    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.head.data
    
    def display_Stack(self):
        current = self.head
        if(self.isEmpty()):
            return None
        else:
            size = 0
            while(current.next != None):
                print(current.data,"-->",end = " ")
                current = current.next
                size +=1
        return ({"Size":size})

if __name__ == "__main__":
    MyStack = Stack()
 
    MyStack.push(11) 
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
    
    a = MyStack.display_Stack()
    print(a)
    
    print("\nTop element is ---->",MyStack.peek())
    
    MyStack.pop()
    MyStack.pop()
    
    a = MyStack.display_Stack()
    print(a)
    
    print("\nTop element is ", MyStack.peek(),"\n") 
    print(MyStack.isEmpty())
    
