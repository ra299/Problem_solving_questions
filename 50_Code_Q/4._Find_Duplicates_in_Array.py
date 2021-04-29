# def find(arr, size):
#     print("Duplicates values are....")

#     for i in range(0, size):
#         # if arr[abs(arr[i])] >= 0:
#         if arr[abs(arr[i])] >= 0:
#             arr[abs(arr[i])] = - arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]), end = " ")

# if __name__ == "__main__":
#     arr = [1, 2, 3, 1, 3, 6, 6,12,12]
#     size = len(arr)
#     find(arr, size)

def find(arr):
    resultSet = []
    for i in range(len(arr)):
        index = abs(arr[i])-1

        if(arr[index]<0):
            resultSet.append(abs(arr[i]))
        else:
            arr[index] = -arr[index]
    
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    return resultSet
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 3, 6, 6,12,12]
    print(find(arr))