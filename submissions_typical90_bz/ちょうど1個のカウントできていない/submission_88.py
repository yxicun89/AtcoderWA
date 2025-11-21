import math
import collections
from collections import Counter, deque, defaultdict
import sys
import copy
import itertools
import re
import bisect
import heapq
from functools import lru_cache
from heapq import heappush, heappop
# import numpy as np
import decimal
from itertools import accumulate
import statistics

from itertools import product
sys.setrecursionlimit(10000000)
INF=10**20
p=10**9+7
list(product([False, True], repeat=3))#2^3通り

# n=int(input())
# a=list(map(int,input().split()))
n,m=map(int,input().split())
ansl=[[] for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    ansl[a-1].append(b-1)
    ansl[b-1].append(a-1)
ans=0
for i in range(n):
    f=0
    for j in ansl[i]:
        if i>j and f==0:
            f=1
        else:f=-1
    if f==1:
        ans+=1
print(ans)

