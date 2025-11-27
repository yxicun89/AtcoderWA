n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sa=0
for i in range(n):
    sa+=abs(A[i]-B[i])

if (sa-k)%2==0:
    print("Yes")
else:
    print("No")