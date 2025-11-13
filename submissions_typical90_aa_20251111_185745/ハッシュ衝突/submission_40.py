import sys
import math
import bisect
#import heapq
import typing
#import numpy as np


input = sys.stdin.readline

def I(): return int(sys.stdin.readline().rstrip())

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

def S(): return sys.stdin.readline().rstrip()

def LS(): return list(sys.stdin.readline().rstrip().split())

#ハッシュ化？

N=I()
T=[S() for _ in range(N)]

K=1000000007
#K=998244353

num_list=[]
num=1
for i in range(16):
    num_list.append(num)
    num=(num*40)%K

User_name=set()

for i in range(N):
    T[i]=list(T[i])
    len_Ti=len(T[i])
    for j in range(len_Ti):
        T_ij=T[i][j]
        if T_ij.isdecimal()==1:
            T[i][j]=int(T_ij)+1
        else:
            T[i][j]=ord(T_ij)-ord('a')+11
    
    hash_num=0
    for j in range(len_Ti):
        hash_num+=T[i][j]*num_list[j]
    hash_num=hash_num%K

    if hash_num not in User_name:
        print(i+1)
        User_name.add(hash_num)