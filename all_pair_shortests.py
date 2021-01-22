num_vert = 100
A = [[[]]]
for k in range(1, num_vert+1):
    for i in range(1, num_vert+1):
        for j in range(1, num_vert+1):
            A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k]+A[k-1][k][j])

