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

    

if __name__ == "__main__":

    l_List = LinkList()
    l_List.head = Node(1)
    second = Node(2)
    third = Node(3)

    l_List.head.next = second
    second.next = third

    l_List.print_list()