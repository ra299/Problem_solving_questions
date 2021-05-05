class ThreeStacks:
    def __init__(self, size):
        self.size = size
        self.lst = [None] * 3 * size
        self.top = [0,0,0]

    def push(self, data, stack_num):
        if(stack_num < 3 and stack_num >=0):
            self.lst[stack_num * self.size + self.top[stack_num]] = data
            self.top[stack_num] +=1

    def pop(self, stack_num):
        if stack_num >=0 and stack_num < 3:
            temp = self.lst[self.top[stack_num]]
            self.lst[self.top[stack_num]] = None
            self.top[stack_num]-=1
 
    # def size(stackNum):
    #     return top[stackNum]


if __name__ == "__main__":
    a = ThreeStacks(3)

    # Stack One Push // First interger is stack value and second interger is stack number
    a.push(1,0)
    a.push(2,0)
    a.push(3,0)

    # Stack Two Push // First interger is stack value and second interger is stack number
    a.push(4,1)
    a.push(5,1)
    a.push(6,1)

    # Stack Three Push // First interger is stack value and second interger is stack number
    a.push(7,2)
    a.push(8,2)
    a.push(9,2)

    print(a.size)
    print(a.lst)
    print(a.top)

    a.pop(2)

    print(a.size)
    print(a.lst)
    print(a.top)

    a.pop(2)

    print(a.size)
    print(a.lst)
    print(a.top)

    