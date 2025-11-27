n,k = map(int,input().split())
a,b = list(map(int,input().split())), list(map(int,input().split()))
g = 0
for i in range(n):
  g += abs(a[i] - b[i])
print("No" if (k-g) % 2 else "Yes")