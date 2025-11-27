N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



dif = 0

for i in range(N):

    dif += abs(A[i] - B[i])



if K % 2 == 1 and  dif % 2 == 1 and dif >= K:

    print("Yes")

elif  K % 2 == 0 and dif % 2 == 0 and dif >= K:

    print("Yes")

else:

    print("No")

