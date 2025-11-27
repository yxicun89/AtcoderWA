#sigh up request
n = int(input())
s = [str(input()) for _ in range(n)]

ans = []
set_s = set()

for i, x in enumerate(s):
  if x not in set_s:
    set_s.add(x)
    ans.append(i) 
    
for h in ans:
  print(h)