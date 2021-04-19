class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def _print_linked_List(self):
        current = self.head
        while(current):
            print(current.data, end = "__")
            current = current.next

    def palindrome_Ulit(self, string):
        return(string == string[::-1])

    def check_Palindrome(self):
        temp = []
        current = self.head
        while(current):
            temp.append(current.data)
            current = current.next
        string = "".join(temp)
        return self.palindrome_Ulit(string)

if __name__  == "__main__":
    llist = Linked_List()
    llist.head = Node('a')
    llist.head.next = Node('bc')
    llist.head.next.next = Node("d")
    llist.head.next.next.next = Node("dcb")
    llist.head.next.next.next.next = Node("a")
    print("True") if llist.check_Palindrome() else "false"
    llist._print_linked_List()
