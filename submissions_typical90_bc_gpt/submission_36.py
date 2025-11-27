
N, P, Q = map(int, input().split())

A = list(map(int, input().split()))



def f(used, n, p):

    if n == 5:

        if p == Q:

            return 1

        else:

            return 0



    if N-1 - used < 5-n:

        return 0



    res = 0

    for i in range(used+1, N):

        res += f(i, n+1, (p + A[i]) % P)



    return res



ans = f(-1, 0, 1)

print(ans)
