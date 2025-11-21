N,K =map(int,input().split())

A= list(map(int,input().split()))
B = list(map(int,input().split()))

cost = 0
for i in range(N):
    cost += A[i]-B[i]
if cost > K:
    print('No')
elif cost % 2 == K % 2:
    print('Yes')
else:
    print('No')