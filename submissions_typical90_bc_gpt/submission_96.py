n,p,q = map(int, input().split())
s = list(map(int, input().split()))
num = 0
for i in range(n):
  for j in range(i):
    for k in range(j):
      for l in range(k):
        for m in range(l):
          if (s[i]%p)*(s[j]%p)*(s[k]%p)*(s[l]%p)*(s[m]%p) == q:
            num += 1
print(num)