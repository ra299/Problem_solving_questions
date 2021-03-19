def sortStack(stack):
    tempStack = createStack()
    while(isEmpty(stack)==False):
        temp = top(stack)
        pop(stack)

        while(isEmpty(tempStack) == False and int(top(tempStack)) > int(temp)):
            push(stack, top(tempStack))
            pop(tempStack)
        push(tempStack, temp)
    return tempStack

def createStack():
    stack = []
    return stack

def isEmpty(stact):
    return len(stact) == 0

def push(stack, item):
    stack.append(item)

def top(stack):
    p = len(stack)
    return stack[p-1]

def pop(stack):
    if isEmpty(stack):
        print("stack underflow")
        exit(1)
    return stack.pop()

def prints(stack):
    for i in range(len(stack)):
        print(stack[i], end = " ")
        print()

if __name__ == "__main__":
    stack = createStack() 
    push( stack, str(8) ) 
    push( stack, str(1) ) 
    push( stack, str(2) ) 
    push( stack, str(5) )
    
    print("Sorted numbers are: ") 
    sortedst = sortStack ( stack ) 
    prints(sortedst) 