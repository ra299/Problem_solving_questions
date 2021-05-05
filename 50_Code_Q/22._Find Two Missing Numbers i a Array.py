def findMissingNumber(arr, n):
    mark = [False for i in range(n+1)] 

    for i in range(0, n-2, 1):
        mark[arr[i]] = True

    for i in range(1, n-1):
        if(mark[i] == False):
            print(i, end = " ")
    print("\n")

if __name__ == "__main__":
    arr = [0,3,5,6]
    n = len(arr) + 2

    findMissingNumber(arr, n)