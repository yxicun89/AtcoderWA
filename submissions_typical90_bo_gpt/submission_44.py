def base8to9(s):
  a = 0
  for d in s:
    a = a * 8 + int(d)
  
  res = ""
  while a > 0:
    a, d = divmod(a, 9)
    res = ("5" if d == 8 else str(d)) + res
  return res if res else "0"
  
N, K = map(int, input().split())
S = str(N)

for i in range(K):
  S = base8to9(S)
  print(S)