n=int(input())
l=set()
for i in range(n):
  s=input()
  if l.isdisjoint(s):
    l.add(s)
    print(i+1)
