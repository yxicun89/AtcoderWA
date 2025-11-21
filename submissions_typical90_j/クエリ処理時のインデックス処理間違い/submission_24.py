n = int(input())

a = 0
b = 0
sa = []
sb = []

C = []
P = []

for i in range(n):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)
    
q = int(input())

L = []
R = []

for i in range(q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    
for i in range(n):
    if C[i] == 1:
        a += P[i]
    else:
        b += P[i]
    
    sa.append(a)
    sb.append(b)

for i in range(q):
    print(str(sa[R[i] - 1] - sa[L[i] - 2]) + ' ' + str(sb[R[i] - 1] - sb[L[i] - 2]))