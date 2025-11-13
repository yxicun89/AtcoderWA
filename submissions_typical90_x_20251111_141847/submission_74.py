# 2回printしてしまっている

import sys



def I(): return int(sys.stdin.buffer.readline())

def LI(): return [int(a) for a in sys.stdin.buffer.readline().decode().split()]

def F(): return float(sys.stdin.buffer.readline())

def LF(): return [float(a) for a in sys.stdin.buffer.readline().decode().split()]

def S(): return sys.stdin.buffer.readline().decode().rstrip()

def LS(): return sys.stdin.buffer.readline().decode().split()

def LM(n, parser=LI): return [parser() for _ in range(n)]



N, K = LI()

A, B = LM(2)



dif = 0



for i in range(N):

    dif += abs(A[i] - B[i])



if dif > K:

    print("No")



if (K - dif) % 2 == 0:

    print("Yes")

else:

    print("No")





