N,P,Q = map(int,input().split())
l = list(map(int,input().split()))

ans = 0

for i in range(N):
    for j in range(N - i - 1):
        for k in range(N - i - j - 2):
            for n in range(N - i - j - k - 3):
                for m in range(N - i - j - k - n - 4):
                    a = l[i]
                    b = l[i + j + 1]
                    c = l[i + j + k + 2]
                    d = l[i + j + k + n + 3]
                    e = l[i + j + k + n + m + 4]
                    if (a * b * c * d * e) % P == Q:
                        ans += 1