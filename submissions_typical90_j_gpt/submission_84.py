N = int(input())
c1 = [0]*N
c2 = [0]*N

for i in range(N):
    c,p = (map(int, input().split()))
    if c ==1:
        c1[i] = p
    else:
        c2[i] = p
s1=[0]*(N+1)
s2=[0]*(N+1)

for i in range(N):
    s1[i+1] = s1[i] + c1[i]
    s2[i+1] = s2[i] + c2[i]


Q = int(input())
L = []
R = []

for i in range(Q):
    l,r = (map(int, input().split()))
    L.append(l)
    R.append(r)

for i in range(Q):
    print(s1[R[i]]-s1[L[i-1]], " ", s2[R[i]]-s2[L[i-1]])