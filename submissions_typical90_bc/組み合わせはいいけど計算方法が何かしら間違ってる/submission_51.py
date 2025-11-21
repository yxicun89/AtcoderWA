N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

import itertools

ans = 0
for v in itertools.combinations([i for i in range(N)], 5):
    temp = 0
    for j in v:
        temp = (temp + A[j])%P
    if temp==Q:
        ans += 1
print(ans)
        