# ソートして順番ずれ

N, K = (int(x) for x in input().split())

A=list(map(int, input().split()))

B=list(map(int, input().split()))

A=sorted(A)

B=sorted(B)

ok=[False]*N



for i in range(N):

    if abs(A[i]-B[i]) <= K:

        K -= abs(A[i]-B[i])

        ok[i] = True

    else:

        ok[i] = False



if ok == [True]*N and K%2 == 0:

    print("Yes")

else:

    print("No")
