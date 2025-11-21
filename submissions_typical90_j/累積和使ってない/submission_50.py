n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
q = int(input())
t = [list(map(int, input().split())) for i in range(q)]
for i in range(q):
  for j in range(t[i][0]-1,t[i][1]):
    num1,num2 = 0,0
    if s[j][0] == 1:
      num1 += s[j][1]
    else:
      num2 += s[j][1]
    print(num1,num2)