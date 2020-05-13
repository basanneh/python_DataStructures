def matrix(m,n):
    result = [[0,0],
            [0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += m[i][k] * n[k][j]


    for i in range(2):
        for j in range(2):
            print(result[i][j], end=' ')
        print()

m =[[1,2],
   [3,4]]

n = [[5,6],
    [7,8]]

matrix(m,n)
