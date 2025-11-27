N,K = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = sum([abs(a[i]-b[i]) for i in range(N)])

if (K-c) % 2 == 0:
    print("Yes")
else:
    print("No")