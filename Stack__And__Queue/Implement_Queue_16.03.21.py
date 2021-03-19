class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None


    def eN_Queue(self,data):
        temp = Node(data)

        if self.rear == None:
            self.rear = self.front = temp
        else:
            self.rear.next = temp
            self.rear = temp
    
    def dE_Queue(self):

        if self.isEmpty():
            return None
        else:
            temp = self.front
            self.front = self.front.next
        if self.front == None:
            self.rear = None

    def display_Queue(self):
        current = self.front
        size = 0
        if self.isEmpty():
            return False
        else:
            while(current != None):
                print(current.data,end = " ")
                current = current.next
                size +=1
        return ({"Size":size})

if __name__ == "__main__":
    q = Queue() 
    q.eN_Queue(10) 
    q.eN_Queue(20) 
    q.eN_Queue(30) 
    q.eN_Queue(40) 
    q.eN_Queue(50)
    a = q.display_Queue()
    print(a)

    q.dE_Queue() 
    q.dE_Queue() 
    a = q.display_Queue()
    print(a)

    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 