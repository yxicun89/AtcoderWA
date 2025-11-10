N = int(input())
s1 = [0]*(N+1)
s2 = [0]*(N+1)

for i in range(1,N+1):
    s1[i],s2[i] = s1[i-1],s2[i-1]
    c,p = map(int, input().split(' '))
    if c == 1:
        s1[i] += p
    else:
        s2[i] += p

Q = int(input())
for _ in range(Q):
    L,R = map(int, input().split(' '))
    r1 = s1[R]-s1[L-1]
    r2 = s2[R]-s2[L-1]

print(' '.join(map(str, (r1,r2))))
