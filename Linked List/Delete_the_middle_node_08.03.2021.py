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
            print(temp.data)
            temp = temp.next

def take_count(head):
    count = 0
    while(head != None):
        count+=1
        head = head.next
    return count

def delete_m(head):
    if(head == None or head.next == None):
        return head

    count = take_count(head)
    copyhead = head
    mid = count // 2
    while(mid > 1):
        mid-=1
        head = head.next
    head.next = head.next.next
    return copyhead

    

if __name__ == "__main__":

    l_List = LinkList()
    l_List.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    l_List.head.next = second
    second.next = third
    third.next = fourth

    l_List.print_list()
    delete_m(l_List.head)
    print("\n")
    l_List.print_list()