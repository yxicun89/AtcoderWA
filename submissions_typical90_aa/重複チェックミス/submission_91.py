n = int(input())
ans = 1
cand = ""
Ans = []
for _ in range(n):
  a = str(input())
  if a in cand:
    pass
  else:
    Ans.append(ans)
    cand = cand + a
  ans += 1
print(*Ans)