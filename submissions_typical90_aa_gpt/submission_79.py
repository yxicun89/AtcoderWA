import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
from collections import deque
import heapq
import math
import bisect
def MI():return map(int,input().split())
def II():return int(input())

N=II()
can=defaultdict(lambda:int)
for i in range(N):
    s=input()
    if not can[s]:
        can[s]=True
        print(i+1)