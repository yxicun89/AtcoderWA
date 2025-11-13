n,k = map(int,input().split())
num = 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(n):
    num += abs(a[i]-b[i])

if (k - num) % 2 == 0:
    print("Yes")
else:
    print("No")