x,y = map(int,input().split())
a = list(map(int,input().split()))	
b = list(map(int,input().split()))
l = [abs(a[i]-b[i]) for i in range(x)]
if (y - sum(l)) % 2 == 0:
  print("Yes")
else:
  print("No")