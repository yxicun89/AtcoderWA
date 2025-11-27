
H, W = map(int, input().split())

A_matrix = []

for i in range(H):

    A = list(map(int, input().split()))

    A_matrix.append(A)

B_sum_row = []

for a in A_matrix:

    B = sum(a)

    B_sum_row.append(B)

# print(B_sum_row)



B_sum_col = []

for j in range(W):

    B = sum(A_matrix[i][j] for i in range(H))

    B_sum_col.append(B)

# print(B_sum_col)



B_matrix = []

for i in range(H):

    B_row = []

    for j in range(W):

        B = B_sum_row[i] + B_sum_col[j]

        B_row.append(B)

    B_matrix.append(B_row)

# print(B_matrix)

for i in range(H):

    print(" ".join(map(str, B_matrix[i])))
