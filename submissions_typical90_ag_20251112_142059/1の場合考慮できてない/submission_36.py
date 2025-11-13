import sys
#simplify stdin
INT = lambda : int(sys.stdin.readline().rstrip())
FLOAT = lambda : float(sys.stdin.readline().rstrip())
MI = lambda : map(int, sys.stdin.readline().rstrip().split())
MF = lambda : map(float, sys.stdin.readline().rstrip().split())
MI_DEC = lambda : map(lambda x:int(x)-1, sys.stdin.readline().rstrip().split())
LI = lambda : list(map(int, sys.stdin.readline().rstrip().split()))
TI = lambda : tuple(map(int, sys.stdin.readline().rstrip().split()))
LF = lambda : list(map(float, sys.stdin.readline().rstrip().split()))
TF = lambda : tuple(map(float, sys.stdin.readline().rstrip().split()))
LI_DEC = lambda : list(map(lambda x: int(x)-1, sys.stdin.readline().rstrip().split()))
TI_DEC = lambda : tuple(map(lambda x: int(x)-1, sys.stdin.readline().rstrip().split()))
LS = lambda : list(sys.stdin.readline().rstrip())
TS = lambda : tuple(sys.stdin.readline().rstrip())
LSS = lambda : sys.stdin.readline().rstrip().split()
IN = lambda :sys.stdin.readline().rstrip()

import math
H, W = MI()
print(math.ceil(H/2)*math.ceil(W/2))

