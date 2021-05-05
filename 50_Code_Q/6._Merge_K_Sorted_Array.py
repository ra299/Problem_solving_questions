from heapq import merge


def mergeK(arr, k):
    l = arr[0]
    for i in range(k-1):
        l = list(merge(l, arr[i+1]))
    print(l)
    return l

def printArray(l):
    print(*l)

if __name__ == "__main__":
    arr =[[2, 6, 12 ],
    [ 1, 9 ],
    [23, 34, 90, 2000 ]]
    k = 3
    
    l = mergeK(arr, k)
    
    printArray(l)