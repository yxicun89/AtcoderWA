# k超えてもいいのに超えた瞬間にNo出力してしまっている

N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



func = 0



for i in range(N):

    func += abs(A[i]-B[i])

    if func > K:

        print("No")

        break



if (K - func) % 2 == 0:

    print("Yes")

else:

    print("No")

