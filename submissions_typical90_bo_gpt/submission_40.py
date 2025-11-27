n,k = map(str,input().split())

for i in range(int(k)):
  n10 = 0
  for j in range(len(n)):
    n10 += int(n[len(n)-1-j])*(8**j)
  n9 = ""
  while n10 > 0:
    k = n10%9
    if k == 8:
      k = 5
    n9 = str(k) + n9
    n10 //= 9
  n = n9
print(n)