import sys
sys.setrecursionlimit(10**8)
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

v = sum(A) - sum(B)
v = abs(v)
if K - v < 0:
  print("No")
elif (K-v) % 2 == 0:
  print("Yes")
else:
  print("No")