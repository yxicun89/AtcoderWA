import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

N,P,Q = mi()
A = li()
ans  = 0
for a1 in range(N):
    for a2 in range(a1+1,N):
        for a3 in range(a2+1, N):
            for a4 in range(a3+1, N):
                for a5 in range(a4+1, N):
                    if (((((((a1*a2)%P)*a3)%P)*a4)%P)*a5)%P==Q:
                        ans += 1

print(ans)