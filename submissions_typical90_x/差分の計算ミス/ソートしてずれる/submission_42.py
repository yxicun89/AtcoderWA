# ソートでずれる
# CP Tenkei90-024 on Wed, 30 Jul 2025



N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

A.sort()

B.sort()



d = 0

for i in range(N):

    d += abs(A[i] - B[i])



if K >= d and (K - d) % 2 == 0:

    print("Yes")

else:

    print("No")

