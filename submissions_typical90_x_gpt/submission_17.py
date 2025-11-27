N,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

num=0
for i in range(N):
    num += abs(A[i] - B[i])
    
if (K-num) % 2 ==0:
    print("Yes")
else:
    print("No")