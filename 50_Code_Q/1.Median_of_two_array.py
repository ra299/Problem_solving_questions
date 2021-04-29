def findMedian(a1,a2):
    arr = margeTwoArray(a1,a2)
    arr.sort()
    if(len(arr) % 2 == 0):
        m1 = len(arr)//2
        m2 = m1-1
        a = arr[m1]+arr[m2]
        return a//2
    else:
        return arr[len(arr)// 2]

def margeTwoArray(a1,a2):
    a1.sort()
    a2.sort()
    for i in a2:
        a1.append(i)
    return a1

if __name__ == "__main__":
    a1 = [1,3]
    a2 = [2]
    print(findMedian(a1,a2))
