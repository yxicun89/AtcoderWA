from itertools import combinations
import math

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for p in combinations(A, 5):
    x = 1
    for y in p:
        x *= y
        x /= P
    if x % P == Q:
        ans += 1

print(ans)
