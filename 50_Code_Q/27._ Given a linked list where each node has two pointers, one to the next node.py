class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def clone(root):
    curr = root
    while(curr != None):
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next

    curr = root
    while(curr != None):
        curr.next.random = curr.random.next
        curr = curr.next.next

    curr = root
    dupList = root.next
    while( curr.next != None):
        temp = curr.next
        curr.next = curr.next.next
        curr = temp
    return dupList

    
def printLinkedList(root):
    current = root
    while(current):
        print('Data =', current.data, ', Random =', current.random.data)
        current = current.next

if __name__ == '__main__':
    original_list = Node(1)
    original_list.next = Node(2)
    original_list.next.next = Node(3)
    original_list.next.next.next = Node(4)
    original_list.next.next.next.next = Node(5)
    
    '''Set the random pointers'''
    
    # 1's random points to 3
    original_list.random = original_list.next.next
    
    # 2's random points to 1
    original_list.next.random = original_list
    
    # 3's random points to 5
    original_list.next.next.random = original_list.next.next.next.next
    
    # 4's random points to 5
    original_list.next.next.next.random = original_list.next.next.next.next
    
    # 5's random points to 2
    original_list.next.next.next.next.random = original_list.next
    
    '''Print the original linked list'''
    print('Original list:')
    printLinkedList(original_list)
    
    '''Create a duplicate linked list'''
    cloned_list = clone(original_list)
    
    '''Print the duplicate linked list'''
    print('\nCloned list:')
    printLinkedList(cloned_list)