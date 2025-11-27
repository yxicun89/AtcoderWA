N = int(input())
S = []
for i in range(N):
  s = input()
  if s in S:
    pass
  else:
    print(i)
    S.append(s)
    