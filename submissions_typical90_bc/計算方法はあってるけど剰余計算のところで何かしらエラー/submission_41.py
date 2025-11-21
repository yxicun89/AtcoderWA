import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            for d in range(c + 1, N):
                for e in range(d + 1, N):
                    if ((a % P) * (b % P) * (c % P) * (d % P) * (e % P)) % P == Q:
                        counter += 1

print(counter)
