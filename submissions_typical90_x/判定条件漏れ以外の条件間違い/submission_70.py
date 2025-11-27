import sys
#import copy
#from itertools import product
import math
input = sys.stdin.readline

N,K=map(int,input().split())
a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))

cnt=0
for i in range(N):
    cnt+= abs(a_list[i]-b_list[i])

if K%2 == cnt%2 and K <= cnt:
    print("Yes")
else:
    print("No")
