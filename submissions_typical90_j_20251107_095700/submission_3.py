# l,rが逆

N = int(input())

ps1 = [0]*(N+1)
ps2 = [0]*(N+1)

for i in range(1,N+1):
  C,p = map(int, input().split())
  ps1[i] = ps1[i-1]+(p if C == 1 else 0)
  ps2[i] = ps2[i-1]+(p if C == 2 else 0)
  
Q = int(input())
for _ in range(Q):
  R,L = map(int,input().split())
  total1 = ps1[R] - ps1[L-1]
  total2 = ps2[R] - ps2[L-1]
  print(f"{total1} {total2}")