N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
count = 0
for i in range(N):
    if A[i] > B[i]:
       count += A[i] - B[i]
    else:
       count += B[i] - A[i]        
if count % 2 == K % 2:
    print("Yes")
else:
    print("No")