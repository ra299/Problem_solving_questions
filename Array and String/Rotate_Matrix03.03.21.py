def rotate(matrix):
    if(len(matrix) == 0 or len(matrix) != len(matrix[0])):
        return("Not Possible")
    n = len(matrix)
    for layer in range(round(n/2)):
        frist = layer
        last = n-1-layer
        i = frist
        for i in range(last):
            offset = i - frist

            top = matrix[i][frist]

            # left --> top
            matrix[i][frist] = matrix[last-offset][frist]

            #bottom --> left
            matrix[last-offset][frist] = matrix[last][last-offset]

            #right --> bottom
            matrix[last-offset][frist] = matrix[i][last]

            # to --> right
            matrix[i][last] = top
    return matrix

matrix =[[1,2],[3,4]]
# matrix =[ 
#             [1, 2, 3], 
#             [4, 5, 6], 
#             [7, 8, 9] 
#         ] 
print(rotate(matrix))
