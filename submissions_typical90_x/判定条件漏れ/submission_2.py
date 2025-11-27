# 総和の条件漏れ
n,k=map(int,input().split())

a=list(map(int,input().split()))

b=list(map(int,input().split()))

gap=0

for i in range(n):

    gap+=abs(a[i]-b[i])

k-=gap

if k%2==0:

    print("Yes")

else:

    print("No")

