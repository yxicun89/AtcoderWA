N = int(input())
mp = {}
sum1,sum2 = 0,0
for i in range(1,N+1):
  mp[i] = list(map(int,input().split()))
Q = int(input())
for j in range(1,Q+1):
  l,r = map(int,input().split())
  for k in range(l,r+1):
    student = mp[k]
    if student[0] == 1:
      sum1 += student[1]
    else:
      sum2 += student[1]
  print(sum1,sum2)