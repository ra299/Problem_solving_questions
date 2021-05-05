def subArrayExists(arr):
    s = set()
    n_sum = 0
    for i in range(len(arr)):
        n_sum+=arr[i]

        if (n_sum == 0 or n_sum in s):
            return True
        s.add(n_sum)
    print(s)
    return False

if __name__ == "__main__":
    arr = [-3, 2, 3, 1, 6]
    n = len(arr)
    if subArrayExists(arr):
        print("Found a sunbarray with 0 sum")
    else:
        print("No Such sub array exits!")