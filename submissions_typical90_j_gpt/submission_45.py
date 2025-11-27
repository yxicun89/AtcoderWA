N = int(input())

c1 = [0]*(N+1)
c2 = [0]*(N+1)
sum_c1 = [0]*(N+1)
sum_c2 = [0]*(N+1)

for i in range(1,N+1):
    c, p = map(int,input().split())
    if c == 1:
        c1[i] = p
        
    else:
        c2[i] = p
        
    
Q = int(input())

for _ in range(Q):
    lr = [list(map(int,input().split()))]
    

for i in range(1,N+1):
    sum_c1[i] = c1[i] + sum_c1[i-1]
    sum_c2[i] = c2[i] + sum_c2[i-1]
    
for l,r in lr:
    print(sum_c1[r]-sum_c1[l-1],sum_c2[r]-sum_c2[l-1])