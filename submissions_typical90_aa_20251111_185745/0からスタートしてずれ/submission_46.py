n=int(input())
ls=set()
for i in range(n):
  q=str(input())
  if q not in ls:
    ls.add(q)
    print(i)
