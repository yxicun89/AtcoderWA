H,W = map(int,input().split())
arr = [[0 for _ in range(W)] for _ in range(H)]

for i in range(0,H,2):
  for j in range(0,W,2):
    arr[i][j] = 1 

for i in range(1,H):
  for j in range(1,W):
    if arr[i-1][j-1] == 1 and arr[i][j] == arr[i-1][j-1]:
      arr[i-1][j-1] = 0

cnt = sum(row.count(1) for row in arr)
print(cnt)