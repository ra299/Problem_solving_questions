def find(arr):
    ans = 0
    count = 0
    arr.sort()
    v = []

    for i in range(0,len(arr)):
        if (arr[i] != arr[i-1]):
            v.append(arr[i])

    for i in range(len(v)):
        if(i > 0 and v[i] == v[i-1]+1):
            count+=1
        else:
            count = 1
        ans = max(ans, count)
    return ans

if __name__ == "__main__":
    arr = [1,9,3,10,10,4,20,20,2]
    print(find(arr))