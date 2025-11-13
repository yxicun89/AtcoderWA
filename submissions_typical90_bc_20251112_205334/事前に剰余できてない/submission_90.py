# 競プロ典型 90問　055 - Select 5（★2）

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a in range(0, N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            for d in range(c + 1, N):
                for e in range(d + 1, N):
                    if (a * b * c * d * e) % P == Q:
                        ans += 1

print(ans)