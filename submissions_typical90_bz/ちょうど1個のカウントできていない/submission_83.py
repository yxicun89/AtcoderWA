n, m = map(int,input().split())

list1 = [[] for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  list1[a-1].append(b-1)
  list1[b-1].append(a-1)
num = 0

for i in range(n):
  tmp=0
  for j in list1[1]:
    if i > j:
      tmp += 1
    if tmp==1:
      num+=1
print(num)