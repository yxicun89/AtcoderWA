N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

# 各項の差がK回またはK-diffが偶数

diff = 0

for i in range(N):

    diff += abs(A[i] - B[i])



if diff == K or (K - diff) % 2 == 0:

    print("Yes")

else:

    print("No")

