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
            print(temp.data, end = " ")
            temp = temp.next

def find__Intersection(list1, list2):
    if(list1 == None or list2 == None):
        return None
    
    result1 = getTilandSize(list1)
    print(result1)
    result2 = getTilandSize(list2)
    print(result2)

    if(result1["tail"] != result2["tail"]):
        return None
    
    if(result1["size"] < result2["size"]):
        shorter = list1
        longer = list2
    else:
        shorter = list2
        longer = list1

    longer = get_Kth_Node(longer, abs(result1["size"]- result2["size"]))
    while(shorter != longer):
        shorter = shorter.next
        longer = longer.next
    return longer

def getTilandSize(_list):
    if(_list == None):
        return None
    size = 1
    current = _list.head
    while(current.next != None):
        size+=1
        current = current.next
    return({"tail":current, "size":size})

def get_Kth_Node(head, k):
    current = head
    while(k <0 and current != None):
        current = current.next
        k-=1
    return current   

if __name__ == "__main__":
    first = LinkList()
    first.head = Node(3)
    a = Node(1)
    b = Node(5)
    c = Node(9)
    d = Node(7)
    e = Node(2)
    f = Node(1)

    first.head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print("First Linked List ---->")
    first.print_list()
    print("\n")

    second = LinkList()

    second.head = Node(4)
    a = Node(6)
    b = Node(7)
    c = Node(2)
    d = Node(1)

    second.head.next = a
    a.next = b
    b.next = c
    c.next = d
    print("Second Linked List ---->")
    second.print_list()
    print("\n")

    print("Intersection---->")
    a = find__Intersection(first,second)
    print(a)
    