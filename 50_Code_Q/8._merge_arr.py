def merge(arr1, arr2, arr1_len, arr2_len):
    i = arr1_len-1
    j = arr2_len-1

    lastIndex = arr1_len + arr2_len -1

    while(j>=0):
        if (i>=0 and arr1[i] > arr2[j]):
            arr1[lastIndex] = arr1[i]
            i-=1
        else:
            arr1[lastIndex] = arr2[j]
            j-=1
        lastIndex-=1

def print_(arr):
    print(*arr)

if __name__ == "__main__":
    size_a = 10
  
    arr1 = [10, 12, 13, 14, 18,None,None,None,None,None]
    arr1_len = 5
    
    arr2 = [16, 17, 19, 20, 22]
    arr2_len = 5
    
    merge(arr1, arr2, arr1_len, arr2_len)
    print_(arr1)