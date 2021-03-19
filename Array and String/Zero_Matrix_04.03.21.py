
# make Zero in given row
def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

# make zero in given column 
def nullifyColumn(matrix, clm):
    for i in range(len(matrix)):
        matrix[i][clm] = 0

# main functio where we calculate our matrix
def setZero(matrix):
    rowHasZero = False
    clmHasZero = False

    # check first row has Zero or not
    for i in range(len(matrix[0])):
        if(matrix[0][i] == 0):
            rowHasZero = True
            break

    #check first colimn has zero or not
    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            clmHasZero = True
            break

    #check zero for rest of the array
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    #nullify row base on first clm
    for i in range(len(matrix)):
        if(matrix[i][0] == 0): 
            nullifyRow(matrix, i)

    # nullify clm based on first row
    for i in range(len(matrix[0])):
        if(matrix[0][i] == 0):
            nullifyColumn(matrix, i)
    
    # Nullify first row
    if(rowHasZero):
        nullifyRow(matrix, 0)

    # Nullify first clm
    if(clmHasZero):
        nullifyColumn(matrix, 0)

matrix =[ 
            [1, 0, 3], 
            [4, 5, 6], 
            [7, 8, 0] 
        ] 
print(matrix)
setZero(matrix)
print(matrix)