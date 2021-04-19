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
    result2 = getTilandSize(list2)

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
    while(k > 0 and current != None):
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
    a = find__Intersection(first.head,second.head)
    print(a)
    
    
#------------- 2nd approch -----------------


# Python3 implementation of the approach

# Link list node
class Node:
	def __init__(self):
		self.data = 0
		self.next = None

# Function to get the intersection point
# of the given linked lists
def getIntersectionNode( head1, head2):

	curr1 = head1
	curr2 = head2

	# While both the pointers are not equal
	while (curr1 != curr2):

		# If the first pointer is None then
		# set it to point to the head of
		# the second linked list
		if (curr1 == None) :
			curr1 = head2
		
		# Else point it to the next node
		else:
			curr1 = curr1.next
		
		# If the second pointer is None then
		# set it to point to the head of
		# the first linked list
		if (curr2 == None):
			curr2 = head1
		
		# Else point it to the next node
		else:
			curr2 = curr2.next
		
	# Return the intersection node
	return curr1.data

# Driver code

# Create two linked lists

# 1st Linked list is 3.6.9.15.30
# 2nd Linked list is 10.15.30
	
# 15 is the intersection point

newNode = None
head1 = Node()
head1.data = 10
head2 = Node()
head2.data = 3
newNode = Node()
newNode.data = 6
head2.next = newNode
newNode = Node()
newNode.data = 9
head2.next.next = newNode
newNode = Node()
newNode.data = 15
head1.next = newNode
head2.next.next.next = newNode
newNode = Node()
newNode.data = 30
head1.next.next = newNode
head1.next.next.next = None

# Print the intersection node
print( getIntersectionNode(head1, head2))

# This code is contributed by Arnab Kundu

    