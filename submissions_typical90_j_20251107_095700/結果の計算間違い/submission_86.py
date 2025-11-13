N = int(input())
Sum1 = [0 for _ in range(N+1)]
Sum2 = [0 for _ in range(N+1)]
for i in range(1,N+1):
    c,p = map(int,input().split())
    if c==1:
        Sum1[i] = Sum1[i-1]+p
        Sum2[i] = Sum2[i-1]
    else:
        Sum1[i] = Sum1[i-1]
        Sum2[i] = Sum2[i-1]+p
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    t1 = Sum1[r]-Sum1[l-1]
    t2 = Sum2[r]-Sum1[l-1]
    print("%d %d"%(t1,t2))