from array import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from decimal import Decimal
from heapq import heapify, heappop, heappush
from itertools import accumulate, chain, combinations, permutations, combinations_with_replacement, product
from math import gcd, factorial, log2, ceil, floor, sin, asin, cos, acos, tan, atan, degrees, sqrt
from pprint import pprint
from random import randrange,randint
import re
from sys import platform, setrecursionlimit, stdin
from time import time
from typing import Iterable, TypeVar, Union
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
#MOD=10**9+7
#MOD=998244353
INF=10**18
def ver_check(*args):print(','.join([a+':'+str(globals()[a]) for a in args]))
debug_print=print if platform=='win32' else lambda *args:args
debug_var_check=ver_check if platform=='win32' else lambda *args:args
input=lambda:stdin.readline().strip()
#input=stdin.readline
setrecursionlimit(10**9)

Q=int(input())
deck=deque()

for q in range(Q):
    t,x=map(int,input().split())
    if t==1:
        deck.append(x)
    elif t==2:
        deck.appendleft(x)
    else:
        print(deck[x-1])








