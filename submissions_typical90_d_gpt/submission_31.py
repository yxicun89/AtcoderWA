import copy

def matrix_sum(A, H, W, h, w):
    matrix_sum = 0
    
    for i in range(H):
        matrix_sum = sum(A[i])

    for j in range(W):
        matrix_sum = matrix_sum + A[h][j]

    print(matrix_sum - A[h][w], end=" ")

# 入力
matrix = []
H , W = map(int, input().split())

for i in range(H):
    A = list(map(int, input().split()))
    matrix = matrix + [A]

matrix_copy = matrix.copy()

matrix_output = copy.deepcopy(matrix)

for i in range(H):
    for j in range(W):
        matrix_sum(matrix, H, W, i, j)

    print()

