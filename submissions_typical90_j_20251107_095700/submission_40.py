N = int(input())
C1 = [0] * (N+1)
C2 = [0] * (N+1)
for i in range(N):
    c, p = map(int,input().split())
    if c == 1:
        C1[i+1] = p
    elif c == 2:
        C2[i+1] = p
        
Q = int(input())
L = []
R = []
for i in range(Q):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
    
from itertools import accumulate
acc_C1 = list(accumulate(C1))
acc_C2 = list(accumulate(C2))

for i in range(Q):
    a = acc_C1[R[i]] - acc_C1[L[i]-1]
    b = acc_C2[R[i]] - acc_C2[L[i]-1]
    
print(a,b)