def searchElement(arr, n, x):
    if (n == 0):
        return False

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == x:
                return arr[i][j]

    return False

if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
    print(searchElement(mat, 4, 48))