class Stack_Of_Plates:
    def __init__(self, capacity):
        self.stacts = [[]]
        if capacity < 1:
            raise NameError("A stack is greater than one.")
        else:
            self.capacity = capacity

    def push(self, item):
        if self.stacts == []:
            self.stacts.append(item)
        else:
            if len(self.stacts[-1]) >= self.capacity:
                self.stacts.append([item])
            else:
                self.stacts[-1].append(item)
    
    def pop(self):

        if self.stacts == []:
            raise NameError("Can't pop an empty stack")
        else:

            popped_data = self.stacts[-1][-1]
            if len(self.stacts[-1]) == 1:
                del self.stacts[-1]
            else:
                del self.stacts[-1][-1]
            return popped_data

    def popAt(self, index):
        if self.stacts == []:
            raise NameError("can't pop an empty stack")
        elif index-1 > len(self.stacts):
            raise NameError("Index is our of range")
        else:
            popped_data = self.stacts[index-1][-1]
            if len(self.stacts[index-1]) == 1:
                del self.stacts[-1]
            elif len(self.stacts) == index:
                del self.stacts[-1][-1]

            # Not clear Part for me

            else:
                self.stacts[index-1][-1] = self.stacts[index][0]
                for i in range(index, len(self.stacts)):
                    for j in range(0, len(self.stacts[i])-1):
                        # Move each element forward/up
                        self.stacts[i][j] = self.stacts[i][j+1]
                    if i < len(self.stacts) -1:
                        self.stacts[i][-1] = self.stacts[i+1][0]
                del self.stacts[-1][-1]

                # if length of stack is empty, delete it
                if len(self.stacts[-1]) == 0:
                    del self.stacts[-1]
            return popped_data


if __name__ == "__main__":
    stack = Stack_Of_Plates(4)
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)
    # stack.push(11)
    # stack.push(12)
    for i in range(1, 13):
        stack.push(i)
    print(stack.stacts)
