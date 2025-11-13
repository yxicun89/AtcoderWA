# 差分で絶対値使ってない

n,k = map(int,input().split())

a = map(int,input().split())

b = map(int,input().split())

dif = sum([ai - bi for ai,bi in zip(a,b)])

if (dif - k) % 2 != 0 or k < dif:

  print("No")

else:

  print("Yes")
