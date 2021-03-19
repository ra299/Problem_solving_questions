class Node:
    def __init__(self, ch):
        self.data = ch
        self.next = None


# fisrt Plaindrom approch . Here we make two string s1 and s2 . irst s1 and then s2 but not same format , s2 is bulid in reverse
# if s1 and s2 same then ok
# def construct(head, s1 = "", s2 = ""):
#     print()
#     if(head is None):
#         return s1, s2
    
#     s1 += head.data
#     s1, s2 = construct(head.next, s1, s2)
#     s2 += head.data

#     return s1,s2

# def check_palindrom(head):
#     s1, s2 = construct(head)
#     return s1 == s2

# Second Plindrom approch, here we check left first to right first and incriment and again check 
def isPalindrome(left, right):
 
    if right is None:
        return True, left
 
    val, left = isPalindrome(left, right.next)
    if not val:
        return False, left
 
    prev_left = left
 
    left = left.next
 
    return prev_left.data == right.data, left
 
if __name__ == '__main__':
 
    head = Node("0")
    head.next = Node("1")
    head.next.next = Node("2")
    head.next.next.next = Node("3")
    head.next.next.next.next = Node("2")
    head.next.next.next.next.next = Node("1")
    head.next.next.next.next.next.next = Node("0")

    # if(check_palindrom(head)):
    #     print("its a Plindrom")
    # else:
    #     print("its not a Plindrom")

    left = head
    if isPalindrome(left, head)[0]:
        print("Linked List is a palindrome.")
    else:
        print("Linked List is not a palindrome.")
