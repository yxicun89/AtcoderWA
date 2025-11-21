N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
L = [list(map(int, input().split())) for _ in range(Q)]

ans = [0]*2

for i in range(Q):
  for j in range(N):
    if (L[i][0] <= (j+1) <=  L[i][1] ) and S[j][0] == 1:
      ans[0] += S[j][1]
    elif (L[i][0] <= (j+1) <=  L[i][1] ) and S[j][0] == 2:
      ans[1] += S[j][1]
    else:
      pass

print(ans[0], ans[1])