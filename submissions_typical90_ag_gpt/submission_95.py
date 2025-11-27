import pypyjit, sys
pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(1000000)

import itertools

H, W = map(int, input().split())

print(((H + 1) // 2) * ((W + 1) // 2))