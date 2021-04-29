def matrixPath(grid):
    N = len(grid)
    M = len(grid[0])

    sum = [[0 for i in range(M+1)] for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            sum[i][j] = max(sum[i-1][j],sum[i][j-1]) + grid[i-1][j-1]
            
    return sum[i][j]

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrixPath(grid))