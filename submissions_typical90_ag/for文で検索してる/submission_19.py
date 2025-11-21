import sys,bisect
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

H,W = mi()
ans = 0
for i in range((H-1)//2+1):
    for j in range((W-1)//2+1):
        ans += 1
print(ans)