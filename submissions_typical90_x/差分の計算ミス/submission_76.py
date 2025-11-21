n, k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sub = sum(i+j for i,j in zip(A,B))
print("Yes" if sub <= k and (sub-k)%2==0 else "No" )