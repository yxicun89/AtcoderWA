import bisect,collections,copy,heapq,itertools,math,string
from collections import deque
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def MS(): return sys.stdin.readline().rstrip().split()
def LS(): return list(sys.stdin.readline().rstrip().split())

n,p,q = MI()
a = LI()
ans = 0
for v in itertools.combinations(a,5):
    if sum(v) % p == q:
        ans += 1
print(ans)