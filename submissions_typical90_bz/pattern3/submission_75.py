import copy
import sys
import math
import bisect
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque


n,m = map(int,input().split())
cnt = 0
l = [[] for i in range(n)]
for _ in range(m):
  a,b = map(int,input().split())
  a,b = a-1,b-1
  l[a].append(b)
  l[b].append(a)

for i in range(n):
  if bisect.bisect_left(l[i],i) == 1:
    cnt += 1

print(cnt)
